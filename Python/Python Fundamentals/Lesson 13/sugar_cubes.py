suger_cubes = input().split(' ')

suger_cubes = list(map(int, suger_cubes))

command = ''

while command != 'Mort':
    inputcom=input().split(' ')
    command = inputcom[0]
    if command == 'Add':
        suger_cubes.append(int(inputcom[1]))
    elif command == 'Remove':
        suger_cubes.remove(int(inputcom[1]))
    elif command == 'Replace':
        index = suger_cubes.index(int(inputcom[1]))
        suger_cubes[index] = int(inputcom[2])
    elif command == 'Collapse':
        value = int(inputcom[1])
        list = []
        for i in suger_cubes:
            if i >= value:
               list.append(i)
        suger_cubes=list
print(' '.join(map(str, suger_cubes)))