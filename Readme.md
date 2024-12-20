**_Assignment 1 - CS 3101: Computer Vision_**

**_Overview_**

This Python script implements a series of image processing and computer vision tasks using OpenCV and Matplotlib.

Loading an image, converting it to grayscale, and plotting its intensity histogram.
Performing image transformations (resize, rotate, and apply Gaussian blur).
Detecting faces using Haar Cascades.
Combining all parts into a single script that processes the image step-by-step and displays the results.

**How to Run the Program**

**Download File:** Download the BSCS0122011265.ZIP file and extract it and open it on the Pycharm IDE.

**Install Dependencies:**
The script requires the following Python libraries:

1. OpenCV (cv2) - for image processing and object detection.
2. Matplotlib - for plotting and visualizing images.
3. Install the required libraries using pip if you haven’t already:

**Prepare the Haar Cascade File:** Download the Haar Cascade XML file for face detection from the OpenCV GitHub repository: haarcascade_frontalface_default.xml.
Ensure that the XML file is placed in the same directory as the Python script.

**Run the Program:** After setting up the environment, run the script

The program will process the image, apply transformations, perform face detection, and display the results in a single figure.

**Libraries and Their Versions**
1. OpenCV: **4.10.0**
2. Matplotlib: **3.9.2**

**Challenges Faced During Implementation**

Image Transformation: Handling different image transformation techniques (resize, rotate, and Gaussian blur) required careful use of OpenCV functions to avoid distortion or loss of quality in the transformed images.

Haar Cascade for Face Detection: Ensuring the face detection model performed accurately on various images involved fine-tuning parameters such as scaleFactor and minNeighbors for optimal results.

Combining All Parts: Integrating all steps into a single program required managing the flow of images and transformations to ensure each part executed correctly and results were visually presented in an organized manner.

**Output Files**

Output Images: The program will generate output images for each transformation step (resized, rotated, blurred) and the final image with detected faces. These will be saved in the directory as:

1. resized_image.jpg
2. rotated_image.jpg
3. gaussian_blur.jpg
4. faces_detected.jpg
5. faces_detected_plot.png
6. output_plot.png
7. transformed_images.png
8. combined_output.png

**Plots:** 

Matplotlib plots displaying the original image, grayscale image, intensity histogram, and transformed images.
