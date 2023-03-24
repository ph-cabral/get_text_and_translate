import cv2
import easyocr
import openai

openai.api_key = "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"

target_language = "es-ES"

reader = easyocr.Reader(["pt"], gpu=False)

image = cv2.imread("./imagen.jpeg")
result = reader.readtext(image, paragraph=True)

for res in result:
    
    text = " ".join(res[1])
    text = text.replace("\n", " ")
    text = text.replace("   ", "+")
    text = text.replace(" -+", "")
    text = text.replace(" ", "")
    text = text.replace("+", " ")
    text = text.lower()
    text = text.strip()


    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Traduce el siguiente texto a {target_language}: \"{text}\""),
        max_tokens=30,
    )

    translation = response.choices[0].text.strip()

    print(text)
    print(translation)
    print('*******************************************************')
 