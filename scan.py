import cv2
import easyocr
import openai
import os 
import pytesseract



with open("apikey.txt", "r") as f:
    api_key = f.read().strip()
 
carpeta = "traducciones"
archivo = "japo.txt"
ruta_archivo = os.path.join(carpeta, archivo)

openai.api_key = api_key

target_language = "es-ES"

reader = easyocr.Reader(["ja"], gpu=False)



image = cv2.imread("./2.jpg")
res = reader.readtext(image, paragraph=True)

result = pytesseract.image_to_string(image, lang='jpn')
print(res)
print(result)

for text in result:
    
    # text = " ".join(res[1])
    # text = text.replace("\n", " ")
    # text = text.replace("   ", "+")
    # text = text.replace(" -+", "")
    # text = text.replace(" ", "")
    # text = text.replace("+", " ")
    # text = text.lower()
    # text = text.strip()
    print(text)
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

# os.mkdir(carpeta)



