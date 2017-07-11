import requests
from PIL import Image
headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": "TOKEN"
}

with open("faces.jpg", "rb") as file:
    image_data = file.read()

print(len(image_data))
print("sending request")
url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
result = requests.post(url, data=image_data, headers=headers)
print("got result")


image = Image.open("faces.jpg")

for face in result.json():
    mask = Image.open("mask.png")
    mask = mask.resize((face['faceRectangle']['width']+40, face['faceRectangle']['height']+40))
    image.paste(mask, (face['faceRectangle']['left']-20, face['faceRectangle']['top']-20), mask)

image.show()