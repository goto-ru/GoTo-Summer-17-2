import requests

headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": "ed949f112a524980ad1907524eb7d32d"
}

with open("faces.jpg", "rb") as file:
    image_data = file.read()

print(len(image_data))
print("sending request")
url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
result = requests.post(url, data=image_data, headers=headers)
print("got result")
print(result.text)