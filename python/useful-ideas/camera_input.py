import os
import cv2

new_bird_dir = r'C:\BlueIris\New'
os.chdir(new_bird_dir)
full_dir = os.listdir()
imgs = []

for aFile in full_dir:
    if aFile[-4:] == '.jpg':
        imgs.append(aFile)

test_img = cv2.imread(imgs[0])
print(test_img.shape) # (1520, 2592, 3)     
cv2.imshow('image', test_img)
cv2.waitKey()


gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', gray_img)
cv2.waitKey()

cv2.imwrite( 'gray_bird.jpg', gray_img)
sharpened = cv2.Canny(gray_img,200,200)
cv2.imshow('sharper', sharpened)
cv2.waitKey()

cv2.imwrite('sharpbird.jpg', sharpened)
binary = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('threshold', binary)
cv2.waitKey()

contours,hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
epsilon = cv2.arcLength(contours[0], True)


bigContours = []
for contour in contours:
    contour_handle = contours[0] if len(contours) == 2 else contours[1]
    area_approx = cv2.contourArea(contour_handle)
    if area_approx > 40:
        bigContours.append(contour)
        print(approx)

cv2.drawContours(gray_img, bigContours, -1, (0,0,255), 1)
cv2.imshow('contours',gray_img)
cv2.waitKey()
