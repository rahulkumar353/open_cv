import cv2

img=cv2.imread('hand3.jpeg',1)
img=cv2.resize(img, (300, 300))

blur=cv2.GaussianBlur(img,(7,7),0)

#blur = cv2.medianBlur(img, 11)

edge=cv2.Canny(blur,40,150)

contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("total no of contours =" + str(len(contours)))

res=cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
