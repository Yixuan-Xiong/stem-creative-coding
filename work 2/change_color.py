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

        # Define the number of bins for the spectrum
        self.number_lines = 50
    
    def interpolate_color(self, t):
        # Interpolate RGB values based on the factor `t`
        for i in range(3):  # Loop through R, G, B channels
            self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)
        return tuple(self.color) 
    
    def draw(self):
        dot.background(dot.black)
        for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
            # Calculate the gradient factor `t` for color interpolation
            t = bin_num / (self.number_lines - 1)
            line_color = self.interpolate_color(t)

            # Calculate the start and end points for the line
            pt1 = (bin_num * 15, dot.height)
            pt2 = (bin_num * 15, dot.height - int(bin_val * 200))

            # Draw the line with the interpolated gradient color
            line(dot.canvas, pt1, pt2, line_color, 2)
    
MySketch()
