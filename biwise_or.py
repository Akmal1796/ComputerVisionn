import cv2

img = cv2.imread("flower1.jpeg")

convert_img = cv2.bitwise_not(img)

cv2.imshow("Original Image", img)
cv2.imshow("Updated Image", convert_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# myimage = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("Flower edited", myimage)
# cv2.imshow("Flower Original", src)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()