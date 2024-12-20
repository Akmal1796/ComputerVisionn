import cv2
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

# Load the Haar Cascade file for face detection
haar_cascade_path = 'haarcascade_frontalface_default.xml'  # Replace with the correct path if necessary
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

if face_cascade.empty():
    raise IOError("Haar Cascade file not found or improperly loaded.")

# Load an image containing human faces
image_path = 'image_with_faces.jpg'  # Replace with your image file path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Image at path '{image_path}' not found.")

# Convert to grayscale for face detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces using Haar Cascades
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Save the image with detected faces
output_path = 'faces_detected.jpg'
cv2.imwrite(output_path, image)

# Convert the image to RGB for Matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image with detected faces using Matplotlib
plt.figure(figsize=(10, 10))
plt.imshow(image_rgb)
plt.title('Detected Faces')
plt.axis('off')
plt.savefig('faces_detected_plot.png')  # Save the figure to a file
