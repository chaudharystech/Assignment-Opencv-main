import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('input.jpeg', 0)

if image is None:
    print("Image not found")
    exit()

image = np.float32(image)

dft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted = np.fft.fftshift(dft)

magnitude = cv2.magnitude(shifted[:, :, 0], shifted[:, :, 1])

magnitude = np.log(1 + magnitude)

magnitude = cv2.normalize(
    magnitude, None, 0, 255, cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)     

cv2.imwrite('output.png', magnitude)

plt.imshow(magnitude, cmap='gray')
plt.title("Magnitude Spectrum")
plt.axis("off")