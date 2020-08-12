total_floors = int(input())
total_rooms = int(input())

for floor in range(total_floors, 0, -1):
    room_type = ''

    if floor == total_floors:
        room_type = 'L'
    elif floor % 2 == 1:
        room_type = 'A'
    else:
        room_type = 'O'

    for room in range(total_rooms):
        print(f'{room_type}{floor}{room}', end= ' ')

    print()
