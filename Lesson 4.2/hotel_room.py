month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < nights_count <= 14:
        studio_price -= 0.5 * studio_price
    elif nights_count > 14:
        studio_price -= 0.3 * studio_price
        apartment_price -= 0.1 * apartment_price
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if nights_count > 14:
        studio_price -= 0.2 * studio_price
        apartment_price -= 0.1 * apartment_price
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    if nights_count > 14:
        apartment_price -= 0.1 * apartment_price

total_studio_price = nights_count * studio_price
total_apartment_price = nights_count * apartment_price

print(f'Apartment: {total_apartment_price:.2f} lv.')
print(f'Studio: {total_studio_price:.2f} lv.')
