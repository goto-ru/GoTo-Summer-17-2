import requests
import lxml.html as html

code = requests.get("http://top-knig.ru/malchiki/")
page = html.fromstring(code.content.decode('utf-8'))

content = page.find_class("content").pop()

texts = []
record = False

for child in content.getchildren():
    if child.tag == "h2" and record:
        break
    if child.tag == "h2":
        record = True
    if record:
        texts.append(child.text_content())
print('\n'.join(texts))
