from PIL import Image

im = Image.open("cat.jpg").convert("RGBA")
pixels = im.load()

for i in range(0,im.width):
    for j in range(im.height):
        r, g, b, a = pixels[i, j]
        av = (r + g + b)//3
        if av < 125:
            pixels[i, j] = (r,0,0,a)
        else:
            pixels[i, j] = (r, g, b, a)

logo_im = Image.open("logo.png").convert("RGBA")

new_height = 5*im.height//12
new_width = int(logo_im.width * new_height/logo_im.height)
logo_im = logo_im.resize((new_width, new_height))

im.paste(logo_im, (im.width - logo_im.width, 0), logo_im)
im.show()
