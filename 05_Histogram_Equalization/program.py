import cv2
import matplotlib.pyplot as plt

image = cv2.imread('input.jpeg', 0)

if image is None:
    print("Image not found")
    exit()

equalized = cv2.equalizeHist(image)

cv2.imwrite('histogram_comparison.png', equalized)

hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([equalized], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(hist1)
plt.title("Before Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.plot(hist2)
plt.title("After Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.savefig("output.png", bbox_inches="tight")

plt.close()