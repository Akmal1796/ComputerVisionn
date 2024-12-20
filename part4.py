import cv2
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

# Part 1: Load and process the image
image_path_part1 = 'flower1.jpeg'  # Replace with your image file path for Part 1
image_part1 = cv2.imread(image_path_part1)

if image_part1 is None:
    raise FileNotFoundError(f"Image at path '{image_path_part1}' not found.")

# Convert BGR to RGB
image_rgb_part1 = cv2.cvtColor(image_part1, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray_image_part1 = cv2.cvtColor(image_part1, cv2.COLOR_BGR2GRAY)

# Compute intensity histogram
histogram_part1 = cv2.calcHist([gray_image_part1], [0], None, [256], [0, 256])

# Part 2: Transform the image
image_path_part2 = 'flower2.jpeg'  # Replace with your image file path for Part 2
image_part2 = cv2.imread(image_path_part2)

if image_part2 is None:
    raise FileNotFoundError(f"Image at path '{image_path_part2}' not found.")

image_rgb_part2 = cv2.cvtColor(image_part2, cv2.COLOR_BGR2RGB)

# Resize to 50%
height, width = image_part2.shape[:2]
resized_image_part2 = cv2.resize(image_rgb_part2, (width // 2, height // 2))

# Rotate by 45 degrees
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image_part2 = cv2.warpAffine(image_rgb_part2, rotation_matrix, (width, height))

# Apply Gaussian blur
gaussian_blur_part2 = cv2.GaussianBlur(image_rgb_part2, (15, 15), 0)

# Part 3: Face detection
haar_cascade_path = 'haarcascade_frontalface_default.xml'  # Replace with your Haar Cascade path
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

if face_cascade.empty():
    raise IOError("Haar Cascade file not found or improperly loaded.")

image_path_part3 = 'image_with_faces.jpg'  # Replace with your image file path for Part 3
image_part3 = cv2.imread(image_path_part3)

if image_part3 is None:
    raise FileNotFoundError(f"Image at path '{image_path_part3}' not found.")

# Convert to grayscale
gray_image_part3 = cv2.cvtColor(image_part3, cv2.COLOR_BGR2GRAY)

# Detect faces
faces_part3 = face_cascade.detectMultiScale(gray_image_part3, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles
for (x, y, w, h) in faces_part3:
    cv2.rectangle(image_part3, (x, y), (x + w, y + h), (255, 0, 0), 2)

image_rgb_part3 = cv2.cvtColor(image_part3, cv2.COLOR_BGR2RGB)

# Combined Visualization
plt.figure(figsize=(20, 15))

# Part 1: Original, Grayscale, and Histogram
plt.subplot(3, 4, 1)
plt.imshow(image_rgb_part1)
plt.title('Part 1: Original Image')
plt.axis('off')

plt.subplot(3, 4, 2)
plt.imshow(gray_image_part1, cmap='gray')
plt.title('Part 1: Grayscale Image')
plt.axis('off')

plt.subplot(3, 4, 3)
plt.plot(histogram_part1, color='black')
plt.title('Part 1: Intensity Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Part 2: Transformed Images
plt.subplot(3, 4, 5)
plt.imshow(image_rgb_part2)
plt.title('Part 2: Original Image')
plt.axis('off')

plt.subplot(3, 4, 6)
plt.imshow(resized_image_part2)
plt.title('Part 2: Resized Image')
plt.axis('off')

plt.subplot(3, 4, 7)
plt.imshow(rotated_image_part2)
plt.title('Part 2: Rotated Image')
plt.axis('off')

plt.subplot(3, 4, 8)
plt.imshow(gaussian_blur_part2)
plt.title('Part 2: Gaussian Blur')
plt.axis('off')

# Part 3: Face Detection
plt.subplot(3, 4, 10)
plt.imshow(image_rgb_part3)
plt.title('Part 3: Detected Faces')
plt.axis('off')

plt.tight_layout()
plt.savefig('combined_output.png')  # Save the combined output to a file