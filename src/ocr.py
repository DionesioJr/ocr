import pytesseract
import numpy as np
import cv2


class Ocr:
    
    def imageToText(self, file_path):
        
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
        

        