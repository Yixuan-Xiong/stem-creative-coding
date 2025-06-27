from dorothy import Dorothy 
from cv2 import line, rectangle

dot = Dorothy() 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw_maze)  
    
    def setup(self):
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
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            line(dot.canvas, (x1, y1), (x2, y2), dot.black, 10)

        rectangle(dot.canvas, (520, 210), (570, 260), (0, 255, 0), -1)

MySketch() 