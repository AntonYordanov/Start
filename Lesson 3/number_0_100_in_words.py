number = int(input())
left_part = number // 10
right_part = number % 10
if number >= 0 and number <= 9:

    if number == 1:
        print('one')
    elif number == 2:
        print('two')
    elif number == 3:
        print('three')
    elif number == 4:
        print('four')
    elif number == 5:
        print('five')
    elif number == 6:
        print('six')
    elif number == 7:
        print('seven')
    elif number == 8:
        print('eight')
    elif number == 9:
        print('nine')

if left_part == 1:
    if right_part == 1:
        print('eleven')
    elif right_part == 2:
        print('twelve')
    elif right_part == 3:
        print('thirteen')
    elif right_part == 4:
        print('fourteen')
    elif right_part == 5:
        print('fifteen')
    elif right_part == 6:
        print('sixteen')
    elif right_part == 7:
        print('seventeen')
    elif right_part == 8:
        print('eighteen')
    elif right_part == 9:
        print('nineteen')
    elif right_part == 0:
        print('ten')
elif left_part >= 2 and left_part <= 9:
    if left_part == 1:
        print('eleven')
    elif left_part == 2:
        print('twenty')
    elif left_part == 3:
        print('thirty')
    elif left_part == 4:
        print('forty')
    elif left_part == 5:
        print('fifty')
    elif left_part == 6:
        print('sixty')
    elif left_part == 7:
        print('seventy')
    elif left_part == 8:
        print('eighty')
    elif left_part == 9:
        print('ninety')

    if right_part == 1:
        print('one')
    elif right_part == 2:
        print('two')
    elif right_part == 3:
        print('three')
    elif right_part == 4:
        print('four')
    elif right_part == 5:
        print('five')
    elif right_part == 6:
        print('six')
    elif right_part == 7:
        print('seven')
    elif right_part == 8:
        print('eight')
    elif right_part == 9:
        print('nine')
    elif right_part == 0:
        print('ten')
else:
    if number >= 100:
        print('hundred')
