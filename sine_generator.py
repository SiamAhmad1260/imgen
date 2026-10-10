import math
import random

def sin_data(frequency: float, ampletude: int, sample_rate: int, height_offset: int, rand_min: int, rand_max: int):
    data = []
    for i in range(sample_rate):
        append = random.randint(rand_min, rand_max)

        value = ampletude * math.sin(2*math.pi*frequency*(i/sample_rate)) + height_offset + append
    
        data.append(int(abs(value)))
        
    return data

def map(row , columne):
    map = [[0,0,1],[1,0,1],[0,1,0]]
    data = [2,3,4]
    for i in range(columne):
        for j in range(row):
            if not map[j][i]== 0:
                map[j][i] = data[i]
    print(map)

