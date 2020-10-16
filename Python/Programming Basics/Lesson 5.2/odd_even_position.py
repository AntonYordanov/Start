import sys

n = int(input())

sum_odd = 0
sum_evens = 0
min_odd = sys.maxsize
min_even = sys.maxsize
max_odd = - sys.maxsize
max_even = - sys.maxsize

for position in range(1, n + 1):
    current_number = float(input())

    if position % 2 == 0:
        sum_evens += current_number

        if current_number > max_even:
            max_even = current_number

        if current_number < min_even:
            min_even = current_number
    else:
        sum_odd += current_number

        if current_number > max_odd:
            max_odd = current_number

        if current_number < min_odd:
            min_odd = current_number

print(f'OddSum={sum_odd:.2f},')
if min_odd != sys.maxsize:
    print(f'OddMin={min_odd:.2f},')
else:
    print(f'OddMin=No,')

if max_odd != - sys.maxsize:
    print(f'OddMax={max_odd:.2f},')
else:
    print(f'OddMax=No,')

print(f'EvenSum={sum_evens:.2f},')
if min_even != sys.maxsize:
    print(f'EvenMin={min_even:.2f},')
else:
    print(f'EvenMin=No,', )
if max_even != - sys.maxsize:
    print(f'EvenMax={max_even:.2f}')
else:
    print(f'EvenMax=No')
