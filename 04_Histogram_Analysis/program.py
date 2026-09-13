import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('input.jpeg', 0)

if image is None:
    print("Image not found")
    exit()

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

value = np.argmax(hist)
print("Intensity with highest frequency:", value)

plt.plot(hist)
plt.xlim([0, 256])
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.savefig("output.png", bbox_inches="tight")

plt.close()