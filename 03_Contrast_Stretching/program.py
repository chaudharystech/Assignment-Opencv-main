import cv2
import numpy as np

img = cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

#for min and max intensity

min_intensity = np.min(img)
max_intensity = np.max(img)

result = ((img - min_intensity) / (max_intensity - min_intensity) * 255).astype(np.uint8)

cv2.imwrite("output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
