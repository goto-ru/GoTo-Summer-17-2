import random

from PIL import Image

im = Image.open("cat.jpg").convert("RGBA")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r, g, b, a = pixels[i, j]

        d = random.randint(-100, 100)
        r = max(min(255, r + d), 0)

        d = random.randint(-100, 100)
        g = max(min(255, g + d), 0)

        d = random.randint(-100, 100)
        b = max(min(255, b + d), 0)

        pixels[i, j] = (r, g, b, a)
im.show()
