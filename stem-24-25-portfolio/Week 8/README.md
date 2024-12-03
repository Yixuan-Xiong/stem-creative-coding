# **Week 8**
This week, I learned the concepts from Week 8 (file: week-lerp-mouse) to design a maze game. The maze will be drawn using the cv2 module, and the player will use the mouse to play it.

## **Drawing the Maze**
Using the cv2 module, I first draw a simple maze and highlight the exit with a distinct color for better visibility. [[View Code](./draw_maze.py)]

```python
def draw_maze(self):
    for wall in self.walls:
        x1, y1, x2, y2 = wall
        line(dot.canvas, (x1, y1), (x2, y2), dot.black, 10)
    rectangle(dot.canvas, (520, 210), (570, 260), (0, 255, 0), -1)
```

## **Controlling the Ball**
Using the functionality from Week 8 `self.pos[0] = int(self.pos[0] + (dot.mouse_x - self.pos[0]) * self.t)`, I create the ball to follow the mouse movement.[[View Code](./ball_maze.py)]

```python
def setup(self):
    self.pos = [0, 0]  
    self.t = 0.1 
    self.ball_radius = 15 
```
## **Improvement of the maze setting**
The basic maze framework is now functional. Next, I implement logic to check for collisions between the ball and the maze walls. If the ball collides with a wall, the player loses. If the ball exits the maze, the player wins. I also add visual effects to indicate the game state: the screen turns red upon losing and green upon winning.

**1. Game Initialization**
```python
# True if the ball collides with a wall
self.game_over = False 
# True if the ball reaches the exit
self.success = False  
```

**2.Checking Wall Collisions**
```python
def check_collision(self):
    for wall in self.walls:
        if wall_y1 - ball_radius <= ball_y <= wall_y1 + ball_radius:
            if wall_x1 <= ball_x <= wall_x2:
                return True
```
Horizontal walls: Checks if the ball's top or bottom edge intersects with the wall's y coordinate, and if the ball's x coordinate is within the wall's range.  
Vertical walls: Checks if the ball's left or right edge intersects with the wall's x coordinate, and if the ball's y coordinate is within the wall's range.
If a collision is detected, `True` is returned, and the game ends with `self.game_over = True`.

**3.Checking Success**
```python
def check_success(self):
    if ball_x > exit_left and ball_x < exit_right:
        if ball_y > exit_top and ball_y < exit_bottom:
            self.success = True
```
Verifies if the ball's x and y coordinates fall within the exit's boundaries.  
If `True`, sets `self.success = True`, signaling the player has won.

**4.Visual Background Feedback**
```python
def draw(self):
    # Set background based on game state
    if self.success:
        # Green background for success
        dot.background(dot.white)
        return
    elif self.game_over:
        # Red background for collision
        dot.background(dot.red)  
        return
    else:
        # White background for normal
        dot.background((255, 255, 255))  

    if self.game_over == False:  
            collision_detected = self.check_collision()
            if collision_detected:
                self.game_over = True

        if self.success == False:  
            success_detected = self.check_success() 
            if success_detected: 
                self.success = True 
```

## **Problem & Solution**
During testing, I encountered an issue with the collision detection in the `check_collision(self)` function. The ball could pass through the walls briefly before the screen turned red, indicating a collision. This issue occurred because I initially wrote the condition as `if wall_y1 <= ball_y <= wall_y1 and if wall_x1 <= ball_x <= wall_x1`, without accounting for the ball’s radius. After incorporating the ball's radius into the calculations, the collision detection worked as expected.  
By refining the collision logic and ensuring the ball’s radius is considered, the maze game now functions correctly.

## **Display**
Here's my final code and presentation: [[View Code](./final_work.py)]

## **Conclusions**
This maze game project demonstrates the effective application of Week 8 concepts, particularly I use mouse interpolation to create a functional and interactive experience. The development process involved several layers of refinement, including maze design, smooth ball movement, and collision and success detection logic. A key takeaway from testing the collision detection is the importance of thorough consideration of all edge cases, as overlooking details can lead to unexpected behavior. While the final implementation achieved its intended goals, I have some additional reflections.

Although the maze design is functional, it is static and lacks the ability to dynamically generate or randomize mazes. Over time, introducing multiple levels with increasing difficulty or adding randomized elements could enhance player engagement and replayability.

Another important consideration is scalability. If the maze becomes more complex, with hundreds of walls, how adaptable is the current system? Are current collision detection methods still valid and applicable to this situation?

By reflecting on these aspects, I recognize areas for improvement and potential future enhancements to create a more dynamic and scalable game experience.