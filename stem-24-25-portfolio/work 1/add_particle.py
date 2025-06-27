from dorothy import Dorothy
from cv2 import circle, rectangle
import numpy as np

dot = Dorothy()

class Particle:
    def __init__(self):
        # Initial position of the particle is tied to current mouse position
        self.x = dot.mouse_x
        self.y = dot.mouse_y
        # Randomized speed for each particle
        self.vx = np.random.randint(-1, 2)  # Horizontal velocity
        self.vy = np.random.randint(-1, 2)  # Vertical velocity

    def move(self):
        # Update particle's position
        self.x = (self.x + self.vx) % dot.width  # Wrap around horizontally
        self.y = (self.y + self.vy) % dot.height  # Wrap around vertically

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.particles = []  # List to store particles
        # Define colors for interpolation
        self.start_color = [0, 255, 255]
        self.end_color = [128, 0, 128]  
        self.color = [0, 0, 0] 

    def move_color(self, start_color, end_color, t):
        # Interpolate between start_color and end_color
        for i in range(3):  
            self.color[i] = int(start_color[i] + (end_color[i] - start_color[i]) * t)
        return tuple(self.color)

    def draw(self):
        # Create a semi-transparent layer to fade the trail
        cover = dot.get_layer()
        rectangle(cover, (0, 0), (dot.width, dot.height), dot.black, -1)
        dot.draw_layer(cover, 0.1)

        # Generate a new particle every frame at the mouse position
        self.particles.append(Particle())

        # Limit the number of particles to avoid excessive memory usage
        if len(self.particles) > 200:  # Keep the last 200 particles
            self.particles.pop(0)

        # Update and draw each particle
        for pt in self.particles:
            pt.move()
            # Interpolate the color based on mouse position
            t = dot.mouse_x / dot.width
            color = self.move_color(self.start_color, self.end_color, t)
            # Draw the particle
            circle(dot.canvas, (int(pt.x), int(pt.y)), 10, color, -1)

MySketch()
