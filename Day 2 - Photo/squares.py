import random

from PIL import Image, ImageFilter

im = Image.open("photo.JPG").convert("RGB")
im_result = im.copy()
pixels = im.load()

width = im.width
height = im.height


for i in range(1,4*12):
    im1 = im.crop((i*width//96, i*height//96, (96-i)*width//96+1, (96-i)*height//96+1))
    if i%2==0:
        im1 = im1.filter(ImageFilter.BLUR)
        im1 = im1.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        pixels = im1.load()
        for x in range(im1.width):
            for y in range(im1.height):
                r,g,b = pixels[x,y]
                r,g,b = g,b,r

                d = random.randint(-100, 100)

                r = max(min(255, r + d), 0)
                d = random.randint(-100, 100)

                g = max(min(255, g + d), 0)
                d = random.randint(-100, 100)

                b = max(min(255, b + d), 0)
                im1.putpixel((x,y), (r, g, b))
    im_result.paste(im1, (i*width//96, i*height//96))
im_result.show()