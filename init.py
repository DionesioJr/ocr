from src.ocr import Ocr
import matplotlib.pyplot as plt

ocr = Ocr()


image_path = "./image/meu_teste.jpg"
#image_path = "./image/teste003.jpg"
#image_path = "./image/slide_1.jpg"

image, text = ocr.imageToText(image_path)
image, data = ocr.imageToData(image_path)
image = ocr.boxColor(data, image)

plt.imshow(image)
plt.show()

print(text)
print(data)

#cv2.imshow('image',image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




"""
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
