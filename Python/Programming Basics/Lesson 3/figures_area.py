import  math
figure_type = input()
dimension = float(input())
#square = a * a
#rectangle = l * w
#curcle = π * r2
#triangle =hbb/2
if figure_type == 'rectangle' or figure_type =='triangle':
    dimension2 = float(input())
if figure_type == 'square':
    area = dimension * dimension
if figure_type == 'rectangle':
    area = dimension * dimension2
if figure_type == 'circle':
    area = math.pi * pow(dimension, 2)
if figure_type == 'triangle':
    area = (dimension * dimension2) /2

print(round(area, 3))