from dorothy import Dorothy
from cv2 import line
import math

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        file_path = "stem-24-25-portfolio\\Week 5\\audio\\Chappell Roan - HOT TO GO!_[cut_29sec].wav"
        dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)

        # Define colors 
        self.color = [0, 0, 0]
        self.a = dot.red
        self.b = dot.blue   

        # Number of lines
        self.number_lines = 50

        # Volume scaling
        self.volume = 50

    def interpolate_color(self, t):
        # Interpolate RGB values based on the factor `t`
        for i in range(3):  # Loop through R, G, B channels
            self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)
        return tuple(self.color)

    def draw(self):
        dot.background(dot.black)

        # Baseline height scaling based on mouse x-position
        baseline_scaling = 50 + int(dot.mouse_x / dot.width * 150)

        # Simulate volume fluctuation using a sine wave
        self.volume = 100 + 50 * math.sin(dot.frame / 20)

        # Combine mouse control and sine wave scaling
        total_scaling = baseline_scaling + self.volume

        # Draw spectrum lines
        for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
            t = bin_num / (self.number_lines - 1)
            line_color = self.interpolate_color(t) 

            # Calculate the start and end points of the line
            line_height = int(bin_val * total_scaling)
            pt1 = (bin_num * 15, dot.height)
            pt2 = (bin_num * 15, dot.height - line_height)

            # Draw the line with the interpolated color
            line(dot.canvas, pt1, pt2, line_color, 2)

MySketch()
