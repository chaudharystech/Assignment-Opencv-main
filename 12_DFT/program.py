import cv2
import numpy as np

image = cv2.imread('input.jpeg', 0)

if image is None:
    print("Image not found")
    exit()

image_float = np.float32(image)

dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted_dft = np.fft.fftshift(dft)

magnitude = cv2.magnitude(
    shifted_dft[:, :, 0],
    shifted_dft[:, :, 1]
)

magnitude = np.log(1 + magnitude)

magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

output = np.uint8(magnitude)

cv2.imwrite('output.png', output)

print("Original image shape:", image.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT shape:", shifted_dft.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()