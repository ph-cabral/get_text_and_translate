import cv2
import easyocr
import openai
import os 
from . import key
print(key)
carpeta = "traducciones"
archivo = "japo.txt"
ruta_archivo = os.path.join(carpeta, archivo)

openai.api_key = apikey

target_language = "es-ES"

reader = easyocr.Reader(["ja"], gpu=False)


image = cv2.imread("./1.jpg")
print(1)
result = reader.readtext(image, paragraph=True)


print(result)
for res in result:
    
    text = " ".join(res[1])
    text = text.replace("\n", " ")
    text = text.replace("   ", "+")
    text = text.replace(" -+", "")
    text = text.replace(" ", "")
    text = text.replace("+", " ")
    text = text.lower()
    text = text.strip()

    with open(ruta_archivo, mode="a") as archivo:
        archivo.write(f"***********************\n{text}")

    trad = {'t1':'', 't2':'', 't3':''}
    for l in trad.keys():
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Traduce el siguiente texto a {target_language}: \"{text}\""),
            max_tokens=30,
        )
        trad[l] = response.choices[0].text.strip()
    
    with open(ruta_archivo, mode="a") as archivo:
        archivo.write(f"\n{trad['t1']}\n{trad['t2']}\n{trad['t3']}\n\n\n")
print(1)

# os.mkdir(carpeta)


