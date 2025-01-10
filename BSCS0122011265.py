import cv2
from PIL import Image
import os

# Part 1: Image Compression
def compress_image(input_path, output_path, quality=85):
    try:
        image = Image.open(input_path)
        original_size = os.path.getsize(input_path)
        image.save(output_path, "JPEG", quality=quality)
        compressed_size = os.path.getsize(output_path)
        compression_ratio = original_size / compressed_size
        print(f"Compression successful. Compression Ratio: {compression_ratio:.2f}")
    except Exception as e:
        print(f"Error during image compression: {e}")


# Part 2: Face and Eye Detection
def detect_faces_and_eyes():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)  # Use webcam feed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            cv2.putText(frame, "Face is detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Waiting for face", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow("Face and Eye Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Part 1 Example
    input_image_path = "high_res_2.jpg"
    output_image_path = "compressed_image.jpg"
    compress_image(input_image_path, output_image_path)

    # Part 2 Example
    print("Starting Face and Eye Detection...")
    detect_faces_and_eyes()