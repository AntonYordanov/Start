import sys

n = int(input())
max_number = - sys.maxsize
sum_of_numbers = 0

for index in range(1, n + 1):
    number = int(input())

    if max_number < number:
        max_number = number

    sum_of_numbers += number

sum_of_numbers -= max_number

if sum_of_numbers == max_number:
    print('Yes')
    print(f'Sum = {sum_of_numbers}')
else:
    print('No')
    print(f'Diff = {abs(sum_of_numbers - max_number)}')
