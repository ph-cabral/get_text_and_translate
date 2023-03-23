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


    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Traduce el siguiente texto a {target_language}: \"{text}\""),
        max_tokens=60,
    )

    translation = response.choices[0].text.strip()

    print(text)
    print(translation)
    print('*******************************************************')
  