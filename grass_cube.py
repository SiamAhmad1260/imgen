from image_gen import gen_png
import random

#this will be a square
vertice = 30
data = b''
for i in range(vertice):
    on_row = b'\x00'
    for j in range(vertice):
        r = random.randint(50, 120)
        g = random.randint(170, 255)
        b = random.randint(50, 120)
        a = 255
        pixel = [r,g,b,a]
        pixel = tuple(pixel)
        on_row += bytes(pixel)
    data += on_row
gen_png("grass.png", vertice, vertice, data)

