start = int(input())
end = int(input())
magic_number = int(input())
is_found = False

combination = 0
for first in range(start, end + 1):
    for second in range(start, end + 1):
        combination += 1
        if first + second == magic_number:
            print(f'Combination N:{combination} ({first} + {second} = {magic_number})')
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print(f'{combination} combinations - neither equals {magic_number}')