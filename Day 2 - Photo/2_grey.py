from PIL import Image

im = Image.open("cat.jpg").convert("RGBA")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r, g, b, a = pixels[i, j]
        av = (r + g + b)//3

        # добавляем зеленого
        g = min(255, av + 20)
        b = min(255, av + 20)
        pixels[i, j] = (av, g, b, a)

im.show()
im.save("cat_result.jpg")