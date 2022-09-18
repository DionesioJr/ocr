from PIL import  ImageDraw, Image
import cv2

class ImageTools():
        
    @staticmethod
    def loadFile(file_path):
        image = cv2.imread(file_path)
        return image
        
    @staticmethod
    def writeText(text, image, x, y, size_text=14):
        image_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(image_pil)
        draw.text((x, y), text, size_text)
        image = np.array(image_pil)
        return image_pil
    
    @staticmethod
    def thresholding(image): #limiarização
    
        
        val, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)    
            
        val, thres = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
        
        #adapitativa
        thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 17, 9)
        
        #gaussiliana
        blur = cv2.GaussianBlur(image, (9,9), 0)
        thresh2 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 9)

        return thresh
    
    @staticmethod
    def invertImage(image):
        invert = 255 - image
        return invert
        
    @staticmethod
    def imageToGrey(image):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return image
    
    @staticmethod
    def maximizeImage(image):
        image = cv2.resize(image, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
        return image
        