from dorothy import Dorothy
from cv2 import line

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        file_path = "stem-24-25-portfolio\Week 5\\audio\Chappell Roan - HOT TO GO!_[cut_29sec].wav"
        dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)

        # Define colors 
        self.color = [0, 0, 0]
        self.a = dot.red
        self.b = dot.blue   

        # Number of lines
        self.number_lines = 50

    def interpolate_color(self, t):
        # Use to interpolate r g and b values
        for i in range(3):  # Loop through R, G, B channels
            self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)
        return tuple(self.color) 

    def draw(self):
        dot.background(dot.black)

        # Dynamically adjust the height scaling based on the mouse's x-position
        # GPT
        height_mouse = 50 + int(dot.mouse_x / dot.width * 150)

        # Draw spectrum lines
        for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
            # Interpolation factor for gradient (t ranges from 0 to 1 across the spectrum)
            t = bin_num / (self.number_lines - 1)
            line_color = self.interpolate_color(t)  # Calculate gradient color

            # Calculate the start and end points of the line
            pt1 = (bin_num * 15, dot.height)
            pt2 = (bin_num * 15, dot.height - int(bin_val * height_mouse))

            # Draw the line with the interpolated color
            line(dot.canvas, pt1, pt2, line_color, 3)

MySketch()