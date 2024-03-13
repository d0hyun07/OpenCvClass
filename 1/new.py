import cv2

print(cv2.__version__)

img = cv2.imread('image.jpg') # 이미지 변수 지정

cv2.imshow('woodong', img) # 이미지 창에 어떻게 띄울껀지

cv2.waitKey(0)

cv2.destroyAllWindows()


