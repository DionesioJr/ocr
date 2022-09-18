import pytesseract
from pytesseract import Output
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2



class Ocr:
    
    """
    --psm
    
    Modos de segmentação de página:
       0 Somente orientação e detecção de script (OSD).
       1 Segmentação automática de páginas com OSD.
       2 Segmentação de página automática, mas sem OSD ou OCR. (não implementado)
       3 Segmentação de página totalmente automática, mas sem OSD. (Predefinição)
       4 Suponha uma única coluna de texto de tamanhos variáveis.
       5 Suponha um único bloco uniforme de texto alinhado verticalmente.
       6 Suponha um único bloco uniforme de texto.
       7 Trate a imagem como uma única linha de texto.
       8 Trate a imagem como uma única palavra.
       9 Trate a imagem como uma única palavra em um círculo.
      10 Trate a imagem como um único caractere.
      11 Texto esparso. Encontre o máximo de texto possível em nenhuma ordem específica.
      12 Texto esparso com OSD.
      13 Linha bruta. Trate a imagem como uma única linha de texto,
            ignorando hacks específicos do Tesseract.
    
    """

    config_tesseract = '--tessdata-dir tessdata --psm 4'
    config_tesseract = '--tessdata-dir tessdata'
    lang = 'por'
    min_conf = 1
    
    
    
    def imageToText(self, file_path):
        image = self.loadFile(file_path)
        text = pytesseract.image_to_string(image, lang=self.lang, config=self.config_tesseract)
        return image, text
    
    def imageToOsd(self, file_path):
        image = self.loadFile(file_path)
        text = pytesseract.image_to_string(image, lang=self.lang, config=self.config_tesseract)
        return image, text
    
    def imageToData(self, file_path):
        image = self.loadFile(file_path)
        data = pytesseract.image_to_data(image, lang=self.lang, config=self.config_tesseract, output_type=Output.DICT)
        return image, data
        
    
    def loadFile(self, file_path):
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
    
    def boxColor(self, data, image, color = (255,100,0), write_Text=False):
        
        for i in range(len(data['text'])):
            
            if(data['conf'][i] > self.min_conf):
                
                x = data['left'][i]
                y = data['top'][i]
                w = data['width'][i]
                h = data['height'][i]
                text = data['text'][i]
                
                if(not text.isspace() and len(text) > 0):
                    cv2.rectangle(image, (x,y), (x + w, y + h), color, 2)
                    
                    if(write_Text == True):
                        image = self.writeText(text, image, x, y)
                
        return image
    
    def writeText(self, text, image, x, y, size_text=14):
        
        image_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(image_pil)
        draw.text((x, y), text, size_text)
        image = np.array(image_pil)
        return image_pil
        
        