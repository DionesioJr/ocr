import cv2

class Thresholding:
       
    @staticmethod
    def otsu(image):
        #val, thres = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
        val, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return image
    
    staticmethod
    def gaussian(image):
        image = cv2.GaussianBlur(image, (9,9), 0)
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 9)
        return image
    
    def adaptive(image):
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 17, 9)
        return image