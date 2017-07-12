import requests
import lxml.html as html

def get_bands(name):
    return name.replace('.', '').lower().split(',')

url = "http://darkside.ru/show/index.phtml?cp={0}"
bands = {}
for cp in range(0, 8461, 141):
    print(cp)
    code = requests.get(url.format(cp))
    page = html.fromstring(code.content)

    #жирные
    concerts = page.find_class('titleshow')

    for concert in concerts:
        title = concert.text_content()
        artists = get_bands(title)
        for name in artists:
            if name in bands:
                bands[name] += 1
            else:
                bands[name] = 1

    #обычные
    concerts = page.find_class('titles')
    for concert in concerts:
        title = concert.find('./a').text_content()
        artists = get_bands(title)
        for name in artists:
            if name in bands:
                bands[name] += 1
            else:
                bands[name] = 1

sorted_bands = sorted(bands.items(), key=lambda x:x[1], reverse=True)
for band in sorted_bands[:100]:
    print("{0} - {1}".format(band[0], band[1]))