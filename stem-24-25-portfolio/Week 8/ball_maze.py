from dorothy import Dorothy
from cv2 import line, rectangle, circle

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)  # Include `self.draw` for rendering updates
    
    def setup(self):
        # Define maze walls
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

        # Ball properties
        self.pos = [0, 0] 
        self.t = 0.1 
        self.ball_radius = 15 

    def draw_maze(self):
        # Draw maze walls
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            line(dot.canvas, (x1, y1), (x2, y2), dot.black, 10)

        # Draw the green rectangle (exit area)
        rectangle(dot.canvas, (520, 210), (570, 260), (0, 255, 0), -1)

    def draw(self):
        dot.background(dot.white)
        self.draw_maze()
        # Update ball position based on mouse position
        self.pos[0] = int(self.pos[0] + (dot.mouse_x - self.pos[0]) * self.t)
        self.pos[1] = int(self.pos[1] + (dot.mouse_y - self.pos[1]) * self.t)

        # Draw the ball
        circle(dot.canvas, self.pos, self.ball_radius, dot.blue,-1)

MySketch()
