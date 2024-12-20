import cv2
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt

# 1. Load an image using OpenCV
image_path = 'flower1.jpeg'  # Replace 'image.jpg' with your image file path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Image at path '{image_path}' not found.")

# Convert from BGR to RGB for proper display in Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 2. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Compute the intensity histogram of the grayscale image
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# 4. Plot the images and histogram using Matplotlib
plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Grayscale image
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Intensity histogram
plt.subplot(1, 3, 3)
plt.plot(histogram, color='black')
plt.title('Intensity Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('output_plot.png')  # Save the plot to a file
