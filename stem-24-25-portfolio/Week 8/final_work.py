from cv2 import circle, line, rectangle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        # Ball properties
        self.pos = [0, 0]  
        self.t = 0.1 
        self.ball_radius = 15 
        # Collision state
        self.game_over = False 
        # Reached state
        self.success = False 

        # Maze Walls
        self.walls = [
            # Outside
             # Top
            (150, 50, 500, 50), 
             # Left
            (150, 50, 150, 180), 
            (150, 250, 150, 400),  
             # Right
            (500, 50, 500, 200), 
            (500, 270, 500, 400),  
             # Bottom
            (150, 400, 500, 400), 
            # Inside
            (150, 250, 210, 250), 
            (220, 320, 340, 320),  
            (340, 320, 340, 200),  
            (280, 250, 340, 250),  
            (280, 250, 280, 100),
            (280, 180, 220, 180), 
            (220, 180, 220, 120), 
            (220, 120, 150, 120), 
            (410, 320, 410, 200),  
            (410, 270, 500, 270),  
            (410, 50, 410, 120),  
            (410, 120, 340, 120),  
        ]

    def draw_maze(self):
        # Draw the maze walls
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            line(dot.canvas, (x1, y1), (x2, y2), dot.black, 10)
        # Draw the exit area (green square)
        rectangle(dot.canvas, (520, 210), (570, 260), (0, 255, 0), -1)

    def check_collision(self):
    # Check if the ball collides with any walls
        # Get ball position and radius
        ball_x = self.pos[0]
        ball_y = self.pos[1]
        ball_radius = self.ball_radius
        # Loop through each wall to check for collisions
        for wall in self.walls:
            wall_x1 = wall[0]
            wall_y1 = wall[1]
            wall_x2 = wall[2]
            wall_y2 = wall[3]

            # Check if the wall is horizontal
            if wall_y1 == wall_y2:
                # Check if the ball's top or bottom edge is within the wall's height range
                if wall_y1 - ball_radius <= ball_y <= wall_y1 + ball_radius:
                    # Check if the ball's horizontal position overlaps with the wall's x range
                    if wall_x1 <= ball_x <= wall_x2:
                        return True 
            
            # Check if the wall is vertical
            if wall_x1 == wall_x2:
                # Check if the ball's left or right edge is within the wall's width range
                if wall_x1 - ball_radius <= ball_x <= wall_x1 + ball_radius:
                    # Check if the ball's vertical position overlaps with the wall's y range
                    if wall_y1 <= ball_y <= wall_y2:
                        return True

        # No collision detected with any wall
        return False

    def check_success(self):
    # Check if the ball reaches the exit area
        # Get the ball's position
        ball_x = self.pos[0]  # Ball's x-coordinate
        ball_y = self.pos[1]  # Ball's y-coordinate

        # Define the exit area's boundaries
        exit_left = 520   
        exit_right = 570  
        exit_top = 210    
        exit_bottom = 260 

        # Check if the ball is inside the exit area
        if ball_x > exit_left and ball_x < exit_right:  # Check x-coordinate
            if ball_y > exit_top and ball_y < exit_bottom:  # Check y-coordinate
                self.success = True

    def draw(self):
        # Set background based on game state
        if self.success:
            # Green background for success
            dot.background((0, 255, 0))
            return
        elif self.game_over:
            # Red background for collision
            dot.background(dot.red)  
            return
        else:
            # White background for normal
            dot.background(dot.white)  

        # Draw the maze
        self.draw_maze()

        # Move the ball smoothly toward the mouse
        self.pos[0] = int(self.pos[0] + (dot.mouse_x - self.pos[0]) * self.t)
        self.pos[1] = int(self.pos[1] + (dot.mouse_y - self.pos[1]) * self.t)

        # Check for collision and success
        if self.game_over == False:  
            collision_detected = self.check_collision()
            if collision_detected:
                self.game_over = True

        if self.success == False:  
            success_detected = self.check_success() 
            if success_detected: 
                self.success = True 

        # Draw the ball
        circle(dot.canvas, self.pos, self.ball_radius, dot.blue, -1)

MySketch()
