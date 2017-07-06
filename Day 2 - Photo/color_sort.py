from PIL import Image, ImageFilter

im = Image.open("cat.jpg").convert("RGBA")
im_result = im.copy()

width = im.width
height = im.height
pixels = im.load()

def brightness(pixel):
    r,g,b,a=pixel
    return (r+g+b)//3


def sort(array, row, size):
    for i in range(size-1):
        for j in range(size-1-i):
            if brightness(array[j, row]) > brightness(array[j+1, row]):
                t = array[j, row]
                array[j, row] = array[j+1, row]
                array[j+1, row] = t


for line in range(height):
    print(line)
    sort(pixels, line, width)



im.show()
