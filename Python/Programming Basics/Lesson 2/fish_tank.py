lenght = int (input())
width = int (input())
heigth = int (input())
volume = float (input())
total_volume = lenght*width*heigth
litters = total_volume*0.001
percent = volume/100
total_water = litters - percent * litters
print(total_water)