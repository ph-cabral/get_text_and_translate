# # Importar la librería de Tesseract OCR
# import pytesseract

# # Definir la ruta de la imagen
# img_path = 'imagen.jpeg'

# # Cargar la imagen y usar Tesseract para extraer el texto
# text = pytesseract.image_to_string(img_path)

# # Imprimir el texto extraídome dio este
# print(text)



###############################################################################################################

import cv2
import easyocr
import openai

openai.api_key = "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"

target_language = "es-ES"

reader = easyocr.Reader(["pt", "en"], gpu=False)

image = cv2.imread("./imagen.jpeg")
result = reader.readtext(image, paragraph=True, detail=0)

for res in result:
    
    text = " ".join(res)
    # text = text.replace("\n", " ")
    # text = text.replace(" -  ", "")
    # text = text.replace("  ", " ")
    # text = text.strip()
    text = text.replace(' ', '').replace('-', '').replace('  ', ' ').strip()


    # response = openai.Completion.create(
    #     engine="text-davinci-002",
    #     prompt=(f"Traduce el siguiente texto a {target_language}: \"{text}\""),
    #     max_tokens=60,
    # )

    
    # # cv2.rectangle(image, p0, (p1[0], p0[1] - 23), (166, 56, 242), -1)
    # # cv2.putText(image, res[1], (p0[0], p1[1] - 3), 2,.8,  (255, 255, 255), 1)
    # # cv2.rectangle(image, p0, p2, (166, 56, 242), 2)
    # translation = response.choices[0].text.strip()

    print(text)
    # print(translation)
    print('*******************************************************')
    

    
# cv2.imshow("Image", image) cv2.waitKey(0) cv2.destroyAllWindows()

# input("Presione cualquier tecla para salir...")


##############################################################################################

# import cv2
# import easyocr
# import urllib.request
# import numpy as np

# # Configurar EasyOCR
# reader = easyocr.Reader(["pt"], gpu=False)

# # Descargar la imagen desde la URL
# url = "https://mangadex.org/chapter/1833fa95-afd1-40dc-b2f0-5b1ad4119d10/5"
# with urllib.request.urlopen(url) as url_response:
#     img_array = bytearray(url_response.read())
# image = cv2.imdecode(np.asarray(img_array), -1)

# # Leer el texto en la imagen
# result = reader.readtext(image, paragraph=True)

# # Imprimir el texto
# for res in result:
#     print(res[1])
    
# # Mostrar la imagen
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

