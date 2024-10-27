import cv2

cap = cv2.VideoCapture(0)

while True:
    isTrue,frame = cap.read()
    print(isTrue)
    cv2.imshow("window",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
