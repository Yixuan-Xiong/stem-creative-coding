from dorothy import Dorothy
from cv2 import circle, rectangle

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        pass

    def draw(self):
        # Create a semi-transparent layer to fade out the trail
        cover = dot.get_layer()  # Create a layer matching the canvas size
        rectangle(cover, (0, 0), (dot.width, dot.height), dot.black, -1)  # Black layer for fading
        dot.draw_layer(cover, 0.2) 

        # Draw the circle controlled by the mouse
        x = dot.mouse_x
        y = dot.mouse_y
        radius = 20
        circle(dot.canvas, (x, y), radius, dot.white, -1)  # Draw the circle in white

MySketch()
