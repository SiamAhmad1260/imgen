from image_gen import gen_png
import random
from sine_generator import sin_data
#this will be a square
vertice = 30
data = b''

sine = sin_data(8, 3, vertice, 7, 6, 7)
print(sine)
for i in range(vertice):
    on_row = b'\x00'
    for j in range(vertice):
        if i > sine[j]:
            r = random.randint(100, 130)
            g = random.randint(55, 77)
            b = random.randint(23, 37)
            a = 255
            pixel = [r,g,b,a]
            pixel = tuple(pixel)
            on_row += bytes(pixel)
        else:
            r = random.randint(50, 120)
            g = random.randint(170, 255)
            b = random.randint(50, 120)
            a = 255
            pixel = [r,g,b,a]
            pixel = tuple(pixel)
            on_row += bytes(pixel)
    data += on_row
gen_png("grass_soil.png", vertice, vertice, data)