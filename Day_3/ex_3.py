import cv2

cap = cv2.VideoCapture(0)
while(cap.isOpened()):

    ret, frame= cap.read()
    frame_gray=cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    blur=cv2.GaussianBlur(frame,(3,3),0)
    edge=cv2.Canny(blur,50,150)
    cv2.imshow('frame',frame_gray)
    cv2.imshow('Result',edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()

