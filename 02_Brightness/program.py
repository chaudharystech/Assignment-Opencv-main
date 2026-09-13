import cv2
import numpy as np

image = cv2.imread('input.jpeg')

if image is None:
    print("Image not found")
    exit()

brightness = 50

result = cv2.add(image, np.ones(image.shape, dtype=np.uint8) * brightness)

print("Pixel before:", image[100, 100])
print("Pixel after:", result[100, 100])

cv2.imwrite('output.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
