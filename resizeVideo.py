import cv2

framehight = 1080
framewidth = 1440

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4,framehight)

while True:
    isopen,frame = cap.read()
    cv2.imshow("Image", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()