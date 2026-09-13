import cv2

image = cv2.imread('input.jpeg')

if image is None:
    print("Image is not found")
    exit()

    #GrayScale
result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Original image shape:", image.shape)
print("Grayscale image shape:", result.shape)

height, width = result.shape
print("Height:", height)
print("Width:", width)

cv2.imwrite('output.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
