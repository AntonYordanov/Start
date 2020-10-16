width = int(input())
lenght = int(input())
height = int(input())

room_area = width * lenght * height
space_needed = 0

while True:
    line = input()

    if line =='Done':
        break

    current_box_space = int(line)
    space_needed += current_box_space

    if space_needed > room_area:
        break

if space_needed > room_area:
    print(f'No more free space! You need {space_needed - room_area} Cubic meters more.')
else:
    print(f'{room_area - space_needed} Cubic meters left.')