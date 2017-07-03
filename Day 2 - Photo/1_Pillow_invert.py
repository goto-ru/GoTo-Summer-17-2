from PIL import Image

im = Image.open("cat.jpg").convert("RGBA")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r, g, b, a = pixels[i, j]
        #инверсия
        r = 255 - r
        g = 255 - g
        b = 255 - b
        #добавляем красного
        r = min(255, r + 150)
        pixels[i, j] = (r, g, b, a)

im.show()
im.save("cat_result.jpg")