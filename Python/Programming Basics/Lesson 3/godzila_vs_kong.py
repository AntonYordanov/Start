budget = float(input())
stuntmen_count = int(input())
price_per_clothing = float(input())
decor_price = 0.1 * budget
total_clothing_count = stuntmen_count * price_per_clothing

if stuntmen_count > 150:
    total_clothing_count = 0.9 * total_clothing_count
money_needed = decor_price + total_clothing_count

if money_needed <= budget:
    print('Action!')
    print(f'Wingard starts filming with {(budget - money_needed):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(money_needed - budget):.2f} leva more.')