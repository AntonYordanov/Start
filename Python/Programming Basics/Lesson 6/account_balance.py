line = input()

total_money = 0
while line != 'NoMoreMoney':
    money = float(line)

    if money < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {money:.2f}')
    total_money += money

    line = input()

print(f'Total: {total_money:.2f}')
