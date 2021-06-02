import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../DATA/00-puppy.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img3 = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
cv2.imshow('image', img3)
cv2.waitKey(0)
