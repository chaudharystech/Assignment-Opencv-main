import cv2
import numpy as np

image = cv2.imread('input.jpeg', 0)

if image is None:
    print("Image not found")
    exit()

image_float = np.float32(image)

dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted = np.fft.fftshift(dft)

rows, cols = image.shape
center_row = rows // 2
center_col = cols // 2

mask = np.zeros((rows, cols, 2), np.float32)

size = 50
mask[
    center_row - size:center_row + size,
    center_col - size:center_col + size
] = 1

filtered = shifted * mask

filtered = np.fft.ifftshift(filtered)

result = cv2.idft(filtered)

result = cv2.magnitude(result[:, :, 0], result[:, :, 1])

result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)

result = np.uint8(result)

cv2.imwrite('output.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()