import cv2
import random
img = cv2.imread('assets/logo.jpg', -1)

print(type(img))
print(img.shape)
print(img[257][400])

'''for i in range(300): #change colour
    for j in range(img.shape[1]):
        
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]'''
        

tag = img[300:500, 500:700]
img[100:300, 300:500] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()