import cv2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. Load an image using OpenCV
image_path = 'flower2.jpeg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Image at path '{image_path}' not found.")

# Convert from BGR to RGB for proper display in Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 1. Resize the image to 50% of its original dimensions
height, width = image.shape[:2]
resized_image = cv2.resize(image_rgb, (width // 2, height // 2))

# 2. Rotate the image by 45 degrees
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (width, height))

# 3. Apply a Gaussian blur to the image
gaussian_blur = cv2.GaussianBlur(image_rgb, (15, 15), 0)

# 4. Save the transformed images as separate files
cv2.imwrite('resized_image.jpg', cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR))
cv2.imwrite('rotated_image.jpg', cv2.cvtColor(rotated_image, cv2.COLOR_RGB2BGR))
cv2.imwrite('gaussian_blur.jpg', cv2.cvtColor(gaussian_blur, cv2.COLOR_RGB2BGR))

# 5. Display all the transformed images in a single figure using Matplotlib
plt.figure(figsize=(20, 10))

# Original image
plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Resized image
plt.subplot(1, 4, 2)
plt.imshow(resized_image)
plt.title('Resized Image (50%)')
plt.axis('off')

# Rotated image
plt.subplot(1, 4, 3)
plt.imshow(rotated_image)
plt.title('Rotated Image (45°)')
plt.axis('off')

# Gaussian blurred image
plt.subplot(1, 4, 4)
plt.imshow(gaussian_blur)
plt.title('Gaussian Blurred Image')
plt.axis('off')

plt.tight_layout()
plt.savefig('transformed_images.png')
