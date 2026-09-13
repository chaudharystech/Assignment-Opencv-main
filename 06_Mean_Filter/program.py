import cv2

image = cv2.imread('input.jpeg')

if image is None:
    print("Image not found")
    exit()

result1 = cv2.blur(image, (3, 3))

result2 = cv2.blur(image, (7, 7))

cv2.imwrite('output.png', result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
