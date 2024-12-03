# **Week 5**
This week, I aimed to explore a function to return the current FFT magnitudes while adding color and interaction variations to enhance this basic feature.

## **Gradient Color Changes**
### **Error**
Using the file (week5-online-fft) provided by my instructor as a foundation, I combined it with concepts from (week 8) to implement gradient color transitions. However, I encountered the error: AttributeError: 'MySketch' object has no attribute 'number_lines'. This happened because the file didn't explicitly define `number_lines`. Upon investigating, I realized the issue stemmed from the use of `t = bin_num / (self.number_lines - 1)`. To fix this, I needed to explicitly define `self.number_lines` in the setup function.

```python
def setup(self):
    self.number_lines = 50

def draw(self):
    for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
        # Calculate the gradient factor `t` for color interpolation
        t = bin_num / (self.number_lines - 1)
        line_color = self.interpolate_color(t)
```
This mistake taught me the importance of definitions. While the problem was eventually fixed, it underscored the value of anticipating dependencies and clearly documenting variables and their roles within the system. After fixing this error, [[View Code](./change_color.py)] achieved colour change from left to right from red to blue.

## **More interaction**
To make the interaction more engaging, I explored additional features, including using the mouse to control the height of the FFT lines. The idea was to make the lines shorter when moving the mouse left and taller when moving it right, adding a fun dynamic element to the visualization. [[View Code](./lines_mouse.py)]

```python
def draw(self):
    # Dynamically adjust the height scaling based on the mouse's x-position
    height_mouse = 50 + int(dot.mouse_x / dot.width * 150)
```
The line `height_mouse = 50 + int(dot.mouse_x / dot.width * 150)` was generated with ChatGPT's assistance.

## **Simulated Volume Changes**
Next, I wanted to make the interaction between visuals and music more interactive. Initially, I planned to control the height of the lines with the mouse and tie it directly to volume levels. Unfortunately, I wasn't able to achieve this. Instead, I opted to simulate volume fluctuations visually using the math module to generate a sine wave for smooth oscillations.

```python
def draw(self):
    # Baseline height scaling based on mouse x-position
    baseline_scaling = 50 + int(dot.mouse_x / dot.width * 150)
    # Simulate volume fluctuation using a sine wave
    self.volume = 100 + 50 * math.sin(dot.frame / 20)
    # Combine mouse control and sine wave scaling
    total_scaling = baseline_scaling + self.volume

    # Draw spectrum lines
    for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
        # Calculate the start and end points of the line
        line_height = int(bin_val * total_scaling)
```
This use of `math` to simulate volume fluctuations was generated with ChatGPT's assistance.

## **A little regret**
After combining the two features, I realized I couldn't fully control the lines to disappear entirely by moving the mouse, but the overall effect still conveyed what I wanted to express.

## **Display**
Here's my final code and presentation: [[View Code](./final_work.py)]

## **Conclusions**
This week, I worked on enhancing FFT-based audio visualizations with gradient color transitions, interactive features, and simulated volume changes. The final result was visually dynamic and interactive, but the process highlighted some challenges, especially in balancing mouse control with automated behavior.

While the mouse control and sine wave simulation worked well on their own, combining them created some conflicts. The mouse couldn’t fully control the line heights because the sine wave simulation overrode it at times. This made the visualization less predictable, which left me wondering: should user input always come first to make the interaction feel more intuitive, or should automation take priority to create a specific rhythm and aesthetic? This is something I’ll be thinking about as I work on improving the project.
