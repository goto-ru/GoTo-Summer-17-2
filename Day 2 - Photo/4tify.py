import random

from PIL import Image, ImageFilter

im = Image.open("cat.jpg").convert("RGB")
im_result = im.copy()

width = im.width
height = im.height

s1 = im.crop((0,0,width,height))
s1 = s1.resize((width//2, height//2))
pixels = s1.load()
for x in range(s1.width):
    for y in range(s1.height):
        r, g, b = pixels[x, y]
        s1.putpixel((x, y), (r, 0, 0))
im_result.paste(s1, (0,0))

s1 = im.crop((0,0,width,height))
s1 = s1.resize((width//2, height//2))
pixels = s1.load()
for x in range(s1.width):
    for y in range(s1.height):
        r, g, b = pixels[x, y]
        s1.putpixel((x, y), (0, g, 0))
im_result.paste(s1, (0,height//2))

s1 = im.crop((0,0,width,height))
s1 = s1.resize((width//2, height//2))
pixels = s1.load()
for x in range(s1.width):
    for y in range(s1.height):
        r, g, b = pixels[x, y]
        s1.putpixel((x, y), (0, 0, b))
im_result.paste(s1, (width//2,0))

s1 = im.crop((0,0,width,height))
s1 = s1.resize((width//2, height//2))
pixels = s1.load()
for x in range(s1.width):
    for y in range(s1.height):
        r, g, b = pixels[x, y]
        s1.putpixel((x, y), (g, 0, b))
im_result.paste(s1, (width//2,height//2))

im_logo = Image.open("flash.png").convert("RGBA")
im_logo = im_logo.resize((width//4, int(height*(width//4)/im_logo.width)))
im_result.paste(im_logo, (width//2-width//8, height//2-im_logo.height//2), im_logo)
im_result.show()