import cv2

img=cv2.imread('dinasour.png')
blur=cv2.GaussianBlur(img.copy(),(19, 17),0)
edge=cv2.Canny(blur,40,150)

cv2.imshow('Result',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()