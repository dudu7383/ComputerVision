import numpy as np
import cv2

imgfile = 'window.jpg'
img = cv2.imread(imgfile,cv2.IMREAD_COLOR)

cv2.imshow('img',img)
cv2.waitKey(0)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
