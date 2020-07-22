age = float(input())
gender = str(input())

if age < 16:
    if gender == 'm':
        print('Master')
    elif gender == 'f':
        print('Miss')
else:
    if gender == 'm':
        print('Mr.')
    elif gender == 'f':
        print('Ms.')
