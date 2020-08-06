width = int(input())
length = int(input())

total_cake_pieces = width * length

while total_cake_pieces > 0:
    line = input()

    if line == 'STOP':
        break
    else:
        new_pieces = int(line)
        total_cake_pieces -= new_pieces

if total_cake_pieces > 0:
    print(f'{total_cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_cake_pieces)} pieces more.')
