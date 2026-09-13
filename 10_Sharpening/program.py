import cv2
import numpy as np

image = cv2.imread('input.jpeg')

if image is None:
    print("Image not found")
    exit()

kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

sharpened = cv2.filter2D(image, -1, kernel)

cv2.imwrite('output.png', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
