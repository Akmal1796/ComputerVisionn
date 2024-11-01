import cv2
import numpy as np

# image = np.zeros((512, 512, 1), np.uint8)
# rectangle = cv2.rectangle(image, (100, 100), (300, 300), (255, 255, 255), -1)
#
# cv2.imshow("Created Image", rectangle)
# cv2.imwrite("before.jpg", rectangle)

# img = cv2.imread("before.jpg")
# updated_image = cv2.bitwise_not(img)
# cv2.imwrite( "after_or.jpg", updated_image)

# img1 = cv2.imread("before.jpg")
# img2 = cv2.imread("after.jpg")
# updated_image_or = cv2.bitwise_or(img1, img2)
# cv2.imwrite("after_or.jpg", updated_image_or)

img1 = cv2.imread("before.jpg")
img2 = cv2.imread("after.jpg")
updated_image_and = cv2.bitwise_and(img1, img2)
cv2.imwrite("after_and.jpg", updated_image_and)

cv2.waitKey(0)
cv2.destroyAllWindows()