city = input()
sale = float(input())
commission = 0

if city == 'Sofia':
    if 0 <= sale <= 500:
        commission = 0.05 * sale
    if 500 < sale <= 1000:
        commission = 0.07 * sale
    if 1000 < sale <= 10000:
        commission = 0.08 * sale
    if sale > 10000:
        commission = 0.12 * sale

if city == 'Varna':
    if 0 <= sale <= 500:
        commission = 0.045 * sale
    if 500 < sale <= 1000:
        commission = 0.075 * sale
    if 1000 < sale <= 10000:
        commission = 0.1 * sale
    if sale > 10000:
        commission = 0.13 * sale

if city == 'Plovdiv':
    if 0 <= sale <= 500:
        commission = 0.055 * sale
    if 500 < sale <= 1000:
        commission = 0.08 * sale
    if 1000 < sale <= 10000:
        commission = 0.12 * sale
    if sale > 10000:
        commission = 0.145 * sale

if sale < 0 or (city != 'Sofia' and city != 'Varna' and city != 'Plovdiv'):
    print('error')

else:
    print(f'{commission:.2f}')
