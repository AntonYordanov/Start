n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())
total_area = n * n
bench_area = m * o
area_to_cover = total_area - bench_area
area_of_tile = w * l
needed_tiles = area_to_cover / area_of_tile
needed_time = needed_tiles * 0.2
print (round(needed_tiles,2 ))
print(round(needed_time, 2))