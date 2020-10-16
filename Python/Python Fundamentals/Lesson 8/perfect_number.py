def is_perfect(n):
    divisior = []
    for num in range(1, n):
        if n % num == 0:
            divisior.append(num)
    if sum(divisior) == n:
        return True
    return False

number = int(input())

if is_perfect(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
