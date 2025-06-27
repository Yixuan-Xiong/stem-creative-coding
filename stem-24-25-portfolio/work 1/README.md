# **Week 3**
This week, I aim to explore the effects of Alpha trails by experimenting with their formation in various directions and colors.  
Additionally, I plan to combine these techniques to create visually dynamic particles, emphasizing smooth particle motion, dynamic behavior, and aesthetically captivating trails.  

## **Mouse-Controlled Interaction**
Inspired by the (week3-final-snow) file, I implemented a mouse-controlled circle that leaves a trail as it moves. The trailing effect is created using a semi-transparent layer `cover = dot.get_layer()`, which gradually fades the older trail while maintaining the most recent movement. This implementation demonstrates basic user interaction and motion, achieving smooth and intuitive mouse-controlled behavior. [[View Code](./circle_mouse.py)]

<video src="media/circle.mouse.mp4" controls width="600"></video>

```python
def draw(self):
    # Create a semi-transparent layer to fade out the trail  
    cover = dot.get_layer() 
    rectangle(cover, (0, 0), (dot.width, dot.height), dot.black, -1)
    dot.draw_layer(cover, 0.2)   

    # Draw the circle controlled by the mouse  
    x = dot.mouse_x  
    y = dot.mouse_y  
    radius = 20  
    circle(dot.canvas, (x, y), radius, dot.white, -1)
```

## **Gradient Color Changes**
To enhance visual appeal, I referred to the (week8-lerp-rgb) file, implementing gradient-based color interpolation. The color of the circle transitions smoothly based on the mouse's horizontal position, creating a dynamic and engaging effect. [[View Code](./change_color.py)]

[](https://git.arts.ac.uk/23040253/Yixuan_Xiong_portfolio-STEM/assets/1195/b6f47824-2e2a-47f0-96b0-4936487d34d0)

```python
def setup(self):
    # Initialize color for interpolation
    self.color = [0, 0, 0] 
    self.a = dot.cyan      
    self.b = dot.magenta  

def draw(self):
    # Interpolate the circle's color based on the mouse's x position
    t = dot.mouse_x / dot.width
    # Use to interpolate r g and b values
    for i in range(3):
        self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)
```
## **Visual Effect**
The basic effect is now realised, but it's not visually obvious. I considered again that the effect of the particles is dispersed in all directions, so I started to improve my code.

## **Adding Particles**
To enable particles to disperse in all directions and have individual life cycles, I defined a `Particle` class to manage the behavior of each particle. This class includes properties such as position, speed, velocity, color, and number, allowing for detailed control over their movement and appearance. [[View Code](./add_particle.py)]

[](https://git.arts.ac.uk/23040253/Yixuan_Xiong_portfolio-STEM/assets/1195/fc14863b-84f5-4f90-a6da-61e788ab803c)

```python
def __init__(self):
    # Initial position of the particle is tied to current mouse position
    self.x = dot.mouse_x
    self.y = dot.mouse_y
    # Randomized integer speed for each particle
    self.speed = np.random.randint(1, 7)
    # Horizontal velocity
    self.vx = np.random.randint(-1, 2)
    # Vertical velocity
    self.vy = np.random.randint(-1, 2)   

def move(self):
    # Update particle's position
    self.x = (self.x + self.vx) % dot.width  # Wrap around horizontally
    self.y = (self.y + self.vy) % dot.height  # Wrap around vertically   

def draw(self):
    self.particles.append(Particle())
    # Keep the last 200 particles
    if len(self.particles) > 200: 
       self.particles.pop(0)

    # Update and draw each particle
    for pt in self.particles:
        pt.move()
        circle(dot.canvas, (int(pt.x), int(pt.y)), 10, color, -1)  
```
## **Problem**
But, there is an issue with particles forming but not disappearing, resulting in the screen being filled with particles. This effect is not what I want, so I googled for a solution. I have found that a life cycle for particles is necessary. By allowing particles to ‘die’ after a limited amount of time, the desired end effect can be achieved.

## **Solution**
**Purpose**: Each particle has a limited lifespan `self.life`, representing the number of frames it can exist for. On each frame, `self.life` is reduced by 1.  
**Outcome**: When self.life reaches 0 or less, the particle `self.particles.remove` and it's removed from the system later.

By introducing a lifespan for particles, I ensured that they disappear over time. This addition significantly improved the system's aesthetics and interaction.

```python
def __init__(self, max_life):
    # Particle's lifespan
    self.life = max_life
    # Maximum lifespan
    self.max_life = max_life

def move(self):
    # Decrease the particle's lifespan
    self.life -= 1

def draw(self):
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
```

After I added a setting for the particle lifecycle, particles now fade and die gracefully over time, enhancing both the visual and interactive effects. This is something I'm very satisfying.  

## **Display**
Here's my final code and presentation: [[View Code](./final_work.py)]

[](https://git.arts.ac.uk/23040253/Yixuan_Xiong_portfolio-STEM/assets/1195/3114c049-6ef5-4556-9f7b-07537310a992)

## **Conclusions**
This week, I focused on combining Alpha trails with gradient color transitions while exploring visually dynamic particle effects. The initial results were encouraging: features like mouse-controlled trails and smooth gradients showed basic interactivity well. However, as the system became more complex, I faced a key problem: the lack of a lifecycle for the particles caused them to stay on the screen indefinitely, resulting in a cluttered and messy visual experience that didn’t match my original aim.

This issue was more than just a technical problem—it showed a gap in my design approach. After thinking it over, I realized that the absence of a defined lifespan for the particles was affecting both the look and functionality of the system. Adding a lifespan solved this by allowing particles to fade out naturally, creating a more smooth and dynamic experience. This change also added a sense of motion and renewal, making the visuals more balanced and pleasing.

This challenge made me rethink some of my original design choices, especially the idea of letting particles stay forever. I realized that this approach didn’t fit with my project aim. Adding lifespans wasn’t just a solution, it also a thoughtful design decision that improved both the look and function of the project, highlighting the motion and visual appeal.

Through updates and small changes, I created a more engaging and smooth interactive experience. This process showed me how important it is to solve problems logically and adjust when needed.Next step, I plan to improve particle fading and motion even more to make the effects look better.