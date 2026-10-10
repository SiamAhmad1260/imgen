from image_gen import gen_png
import random

#this will be a square
vertice = 30
data = b''
for i in range(vertice):
    on_row = b'\x00'
    for j in range(vertice):
        r = random.randint(100, 130)
        g = random.randint(55, 77)
        b = random.randint(23, 37)
        a = 255
        pixel = [r,g,b,a]
        pixel = tuple(pixel)
        on_row += bytes(pixel)
    data += on_row
gen_png("soil.png", vertice, vertice, data)