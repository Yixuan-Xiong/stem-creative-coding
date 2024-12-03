# **Week 7**
This project builds upon the concepts learned in Week 7, particularly from the week7-face-filter file, to create an interactive augmented reality experience. The system utilizes a camera feed to detect faces, overlay sunglasses on detected faces, and introduce falling money bills in the background for a fun and immersive effect.

## **Face Detection with Overlay**
Using the `cv2.CascadeClassifier`, once faces are detected, sunglasses are dynamically resized and positioned on the face based on its width and height.

```python
# Load face detection model
self.face_cascade = cv2.CascadeClassifier("week7/data/haarcascade_frontalface_default.xml")
# Load sunglasses image
self.sunglasses_img = cv2.imread("week7/images/sunglasses.png", cv2.IMREAD_UNCHANGED)  
```

## **Steps to Overlay Sunglasses** ##
**1.Resize the Sunglasses**  
The system uses the Haar Cascade model to detect faces:  

```python
self.face_cascade = cv2.CascadeClassifier("week7/data/haarcascade_frontalface_default.xml")
self.sunglasses_img = cv2.imread("week7/images/sunglasses.png", cv2.IMREAD_UNCHANGED)  
```

The width of the sunglasses is adjusted to match the face's width, while maintaining the aspect ratio for realism: 

```python
sunglasses_resized = cv2.resize(
    self.sunglasses_img, 
    (face_w, int(face_w * self.sunglasses_img.shape[0] / self.sunglasses_img.shape[1]))
)
```

**2.Position**  
·The width of the sunglasses is set to match the face's width.  
·The aspect ratio is maintained for realism.  

```python
eyes_y = face_y + int(face_h * 0.3) - 60
```
Initially, detecting the sunglasses to the eyes was a challenge. Through testing and adjustment, the sunglasses was in a more natural placement.

**3.Overlay**
The `.png` image of the sunglasses contains transparency. To ensure only the non-transparent pixels are drawn, we use pixel-by-pixel checks:

```python
for i in range(sunglasses_height):
    for j in range(sunglasses_width):
        if sunglasses_resized[i, j][3] != 0:  # Non-transparent pixels
            camera_feed[eyes_y + i, face_x + j] = sunglasses_resized[i, j][:3]
```
The implementation required handling the alpha channel (transparency) correctly. With the help of GPT, I implemented nested loops to process each pixel, ensuring proper rendering.

[[View Code](./sunglasses.py)]

[](https://git.arts.ac.uk/23040253/Yixuan_Xiong_portfolio-STEM/assets/1195/149f1e95-4f92-4841-afbe-285dd77b85ce)

## **Falling Bills** ##  
To enhance the augmented reality experience, falling money bills were added as a background effect. Different bill styles and falling speeds create a dynamic visual experience.
**1.Initialization**  
Three different bill images are loaded:

```python
self.bill_images = [
    cv2.imread("week7/images/money1.png", cv2.IMREAD_UNCHANGED),
    cv2.imread("week7/images/money2.png", cv2.IMREAD_UNCHANGED),
    cv2.imread("week7/images/money3.png", cv2.IMREAD_UNCHANGED),
]
```
Each bill is resized for consistency, and its initial position and speed are randomized:

```python
x_positions = np.linspace(0, dot.width, num_bills).astype(int)
y_positions = np.random.randint(-dot.height, 0, num_bills)
```
  
Each bill is assigned:  
· A random x-coordinate.
· A random initial y-coordinate (starting above the visible screen).  
· A random falling speed. 

```python
for x, y in zip(x_positions, y_positions):
    bill_image = random.choice(self.bill_images)
    resized_bill = cv2.resize(bill_image, (bill_width, bill_height))
    self.bills.append({
        "image": resized_bill,
        "x": x,
        "y": y,
        "speed": speed
    })
```

**2.Movement**  
The background includes falling bills randomly positioned and moving at different speeds. This effect enhances the augmented experience.

```python
bill["y"] += bill["speed"]
if bill["y"] > dot.height:
    # Reset to the top
    bill["y"] = random.randint(-dot.height, 0)  
```
**3.Overlay**  
Similar to the sunglasses overlay, non-transparent pixels of the bills are drawn onto the webcam feed.

```python
for i in range(bill_h):
    for j in range(bill_w):
        if bill_img[i, j][3] != 0:  # Non-transparent pixels
            camera_feed[bill["y"] + i, bill["x"] + j] = bill_img[i, j][:3]
```
The implementation required handling the alpha channel (transparency) correctly. With the help of GPT, I implemented nested loops to process each pixel, ensuring proper rendering.

**Problem**  
During runtime, I noticed that my images appeared blue instead of their original red color. This issue arose because the images (e.g., sunglasses.png and bill images) were loaded using `cv2.imread()`, which defaults to the BGR (Blue-Green-Red) color format. However, Dorothy’s canvas operates in the RGB (Red-Green-Blue) format. As a result, when the images were directly overlaid onto the canvas, the red and blue channels were swapped, causing the colors to be distorted.

After google, I learned that the solution involves using `cv2.cvtColor` to convert the images from BGR(A) to RGB(A) format. Despite this insight, my initial attempts at applying the conversion were unsuccessful.

## **Display**
Here's my final code and presentation: [[View Code](./rich_guy.py)]

[](https://git.arts.ac.uk/23040253/Yixuan_Xiong_portfolio-STEM/assets/1195/c7c06df4-8eef-47b7-8cfc-37932531f317)

## **Conclusions**
This Week 7 project combines face detection and augmented reality to create a fun and visually engaging experience. Using Haar cascades, the program detects faces in a live camera feed and dynamically resizes sunglasses to fit perfectly on each face. To add a playful touch, the background features falling money bills that are randomly styled, positioned, and dropped at different speeds, creating a lively and dynamic visual effect.

While the project achieved its main goals, there were some challenges along the way. For instance, the colors of the images were initially distorted due to mismatched formats (BGR vs. RGB). It took extra time and debugging to fix this issue and ensure the images displayed correctly. Additionally, increasing the number of falling bills to 100 caused noticeable lag, pointing to the need for better optimization to handle more complex scenes smoothly.

Right now, the program is more of a passive experience--users watch the effects unfold but don’t interact with them. Adding interactive elements, like allowing users to "catch" the falling bills or influence their movement, could make the experience even more engaging and enjoyable. Addressing the performance issues would also make the application more polished and scalable.
