flowers_type = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers_type == 'Roses':
    price = 5 * flowers_count
    if flowers_count > 80:
        price = 0.9 * price
elif flowers_type == 'Dahlias':
    price = 3.8 * flowers_count
    if flowers_count > 90:
        price = 0.85 * price
elif flowers_type == 'Tulips':
    price = 2.8 * flowers_count
    if flowers_count > 80:
        price = 0.85 * price
elif flowers_type == 'Narcissus':
    price = 3 * flowers_count
    if flowers_count < 120:
        price = price + 0.15 * price
elif flowers_type == 'Gladiolus':
    price = 2.5 * flowers_count
    if flowers_count < 80:
        price = price + 0.2 * price

if budget >= price:
    print(
        f'Hey, you have a great garden with {flowers_count} {flowers_type} and {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(price - budget):.2f} leva more.')
