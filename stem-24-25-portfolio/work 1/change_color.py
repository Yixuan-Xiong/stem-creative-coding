from dorothy import Dorothy
from cv2 import circle, rectangle

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        # Initialize color for interpolation
        self.color = [0, 0, 0] 
        self.a = dot.cyan      
        self.b = dot.magenta  

    def draw(self):
        # Create a semi-transparent layer to fade out the trail
        cover = dot.get_layer()  
        rectangle(cover, (0, 0), (dot.width, dot.height), dot.black, -1) 
        dot.draw_layer(cover, 0.2)

        # Interpolate the circle's color based on the mouse's x position
        t = dot.mouse_x / dot.width  # Fraction of the screen width
        for i in range(3):  # Interpolate RGB channels
            self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)

        # Draw the circle controlled by the mouse
        x = dot.mouse_x
        y = dot.mouse_y
        radius = 20
        circle(dot.canvas, (x, y), radius, tuple(self.color), -1)  # Draw the circle with interpolated color

MySketch()