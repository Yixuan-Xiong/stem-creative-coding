from dorothy import Dorothy
from cv2 import circle, rectangle
import numpy as np

dot = Dorothy()

class Particle:
    def __init__(self, max_life):
        # Initial position of the particle is tied to current mouse position
        self.x = dot.mouse_x
        self.y = dot.mouse_y
        # Randomized integer speed for each particle
        self.speed = np.random.randint(1, 7)
        # Horizontal velocity
        self.vx = np.random.randint(-1, 2)
        # Vertical velocity
        self.vy = np.random.randint(-1, 2) 
        # Particle's lifespan
        self.life = max_life
        # Maximum lifespan
        self.max_life = max_life
        
    def move(self):
        # Update particle's position
        # horizontal direction
        self.x = (self.x + self.vx) % dot.width 
        # vertical direction
        self.y = (self.y + self.vy) % dot.height 
        # Decrease the particle's lifespan
        self.life -= 1

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.particles = []
        # Define colors
        self.start_color = [0, 255, 255] 
        self.end_color = [128, 0, 128]
        self.color = [0, 0, 0]

    def move_color(self, start_color, end_color, t):
        # Use to interpolate r g and b values
        for i in range(3):  
            self.color[i] = int(start_color[i] + (end_color[i] - start_color[i]) * t)
        return tuple(self.color)

    def draw(self):
        # Semi transparent layer to overwrite
        cover = dot.get_layer()
        rectangle(cover, (0, 0), (dot.width, dot.height), dot.black, -1)
        # The higher the alpha, the more opaque the cover, so small alpha makes longer trails 
        dot.draw_layer(cover, 0.1)

        # Generate a new particle every 1 frames at the mouse position
        if dot.frame % 1 == 0:
            # Add a new particle to the self.particles list
            self.particles.append(Particle(max_life=60))
        # Update each particle
        for pt in self.particles:
            # Update the particle's position
            pt.move()
            # Remove the particle if its lifespan is over
            if pt.life <= 0:
                self.particles.remove(pt)
            else:
                # Get x position as fraction of screen 
                t = dot.mouse_x / dot.width
                color = self.move_color(self.start_color, self.end_color, t)
                # Draw the particle
                circle(dot.canvas, (int(pt.x), int(pt.y)), 10, color, -1)

MySketch()
