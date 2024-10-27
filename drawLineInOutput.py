import cv2

cap = cv2.VideoCapture(0)
while True:
    isSuccess, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    cv2.line(frame, (0,0), (width,height), (255, 0, 0), 2)
    cv2.line(frame, (0,height), (width, 0), (255, 0, 0), 2)
    cv2.imshow("video", frame)
    print(isSuccess)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()