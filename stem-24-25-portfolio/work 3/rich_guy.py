import cv2
import random
import numpy as np
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

        # Load bill images
        self.bill_images = [
            cv2.imread("stem-24-25-portfolio\week 7\images\money1.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("stem-24-25-portfolio\week 7\images\money2.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("stem-24-25-portfolio\week 7\images\money3.png", cv2.IMREAD_UNCHANGED),
        ]

        num_bills = 30  # Number of bills
        x_positions = np.linspace(0, dot.width, num_bills).astype(int)
        y_positions = np.random.randint(-dot.height, 0, num_bills)  # Start above the screen
        self.bills = []

        # Initialize bills with positions and properties
        for x, y in zip(x_positions, y_positions):
            bill_image = random.choice(self.bill_images)
            bill_width = 80  # Fixed width
            bill_height = int(bill_width * bill_image.shape[0] / bill_image.shape[1])
            resized_bill = cv2.resize(bill_image, (bill_width, bill_height))
            speed = random.randint(2, 8)  # Random falling speed

            self.bills.append({
                "image": resized_bill,
                "x": x,
                "y": y,
                "speed": speed
            })

    def draw(self):
        success, camera_feed = self.camera.read()  # Capture a frame from the camera
        if success:
            camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))  # Resize the image to fit the canvas
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)  # Convert to RGB
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)  # Convert to grayscale for face detection
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)  # Detect faces

            for face_x, face_y, face_w, face_h in faces:
                # Overlay the sunglasses over the eyes
                sunglasses_resized = cv2.resize(self.sunglasses_img, (face_w, int(face_w * self.sunglasses_img.shape[0] / self.sunglasses_img.shape[1])))
                sunglasses_height, sunglasses_width, _ = sunglasses_resized.shape
                eyes_y = face_y + int(face_h * 0.3) - 60  # Approximate the vertical position of the eyes

                for i in range(sunglasses_height):
                    for j in range(sunglasses_width):
                        if sunglasses_resized[i, j][3] != 0:  # Check if the pixel is not transparent
                            if eyes_y + i >= 0 and eyes_y + i < dot.height and face_x + j >= 0 and face_x + j < dot.width:
                                camera_feed[eyes_y + i, face_x + j] = sunglasses_resized[i, j][:3]  # Add the sunglasses to the image

            # Draw and update bills
            for bill in self.bills:
                bill_img = bill["image"]
                bill_h, bill_w, _ = bill_img.shape

                # Update position (only vertical movement)
                bill["y"] += bill["speed"]

                # Wrap around if the bill exits the bottom
                if bill["y"] > dot.height:
                    bill["y"] = random.randint(-dot.height, 0)  # Reset to the top

                # Draw the bill
                for i in range(bill_h):
                    for j in range(bill_w):
                        if 0 <= bill["y"] + i < dot.height and 0 <= bill["x"] + j < dot.width:
                            if bill_img[i, j][3] != 0:  # Check if the pixel is not transparent
                                camera_feed[bill["y"] + i, bill["x"] + j] = bill_img[i, j][:3]

            dot.canvas = camera_feed  # Display the final image on the canvas

MySketch()
