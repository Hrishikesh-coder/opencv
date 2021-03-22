import cv2

img = cv2.imread('assets/logo.jpg' , -1)

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #resize the image to 1/2 size(0.5)

img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0) #it will wait an infinite amount of time for the user to press any key on the keyboard
cv2.destroyAllWindows()