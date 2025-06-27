import cv2
import random
from dorothy import Dorothy

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)  # Initialize the camera
        self.face_cascade = cv2.CascadeClassifier("stem-24-25-portfolio\week 7\data\haarcascade_frontalface_default.xml")  # Load the face detection model
        self.sunglasses_img = cv2.imread("stem-24-25-portfolio\week 7\images\sunglasses.png", cv2.IMREAD_UNCHANGED)  # Load sunglasses image

    def draw(self):
        success, camera_feed = self.camera.read()  # Capture a frame from the camera
        if success:
            camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))  # Resize the image to fit the canvas
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)  # Convert to RGB
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)  # Convert to grayscale for face detection
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)  # Detect faces

            for face_x, face_y, face_w, face_h in faces:
                # Overlay the sunglasses over the eyes
                sunglasses_resized = cv2.resize(
                    self.sunglasses_img,
                    (face_w, int(face_w * self.sunglasses_img.shape[0] / self.sunglasses_img.shape[1]))
                )
                sunglasses_height, sunglasses_width, _ = sunglasses_resized.shape
                eyes_y = face_y + int(face_h * 0.3) - 60  # Approximate the vertical position of the eyes

                for i in range(sunglasses_height):
                    for j in range(sunglasses_width):
                        if sunglasses_resized[i, j][3] != 0:  # Check if the pixel is not transparent
                            if eyes_y + i >= 0 and eyes_y + i < dot.height and face_x + j >= 0 and face_x + j < dot.width:
                                camera_feed[eyes_y + i, face_x + j] = sunglasses_resized[i, j][:3]  # Add the sunglasses to the image

            dot.canvas = camera_feed  # Display the final image on the canvas

MySketch()
