from PIL import Image
from pytesseract import pytesseract
#define la ruta al archivo tessaract.exe
ruta_tessaract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Define ruta a la imagen
ruta_imagen = 'img/img4.jpg'
#Apuntar tessaract_cmd a la ruta de tessaract.exe
pytesseract.tesseract_cmd = ruta_tessaract
#Abre la imagen con PIL *Python Imaging Library* o "Pillow"
img = Image.open(ruta_imagen)
#Extrae el texto de la imagen.
text = pytesseract.image_to_string(img)
print(text)