from src.ocr import Ocr

import pytesseract
import numpy as np
import cv2
import matplotlib.pyplot as plt




ocr = Ocr()

image_path = "./image/teste01.jpg"
image = ocr.imageToText(image_path)


plt.imshow(image)
plt.show()

#cv2.imshow('image',image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
