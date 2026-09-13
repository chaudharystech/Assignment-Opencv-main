import cv2

image = cv2.imread('input.jpeg')

if image is None:
    print("Image not found")
    exit()

mean = cv2.blur(image, (5, 5))

gaussian = cv2.GaussianBlur(image, (5, 5), 0)

median = cv2.medianBlur(image, 5)

cv2.imwrite('output_mean.png', mean)
cv2.imwrite('output_gaussian.png', gaussian)
cv2.imwrite('output_median.png', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
