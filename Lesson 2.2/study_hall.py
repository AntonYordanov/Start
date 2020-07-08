import math

length = float (input()) * 100
width = float (input()) * 100
rows = math.trunc(length/120)
columns = math.trunc((width - 100)/70)
seats = rows * columns - 3
print(seats)