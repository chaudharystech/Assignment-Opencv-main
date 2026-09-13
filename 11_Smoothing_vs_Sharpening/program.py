import cv2
import numpy as np

image = cv2.imread('input.jpeg')

if image is None:
    print("Image not found")
    exit()

smooth = cv2.GaussianBlur(image, (5, 5), 0)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(image, -1, kernel)

cv2.imwrite('output_smooth.png', smooth)
cv2.imwrite('output_sharp.png', sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
