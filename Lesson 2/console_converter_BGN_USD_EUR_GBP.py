usd_bg_ex_rate = 1.79549
eur_bg_ex_rate = 1.96583
gbp_bg_ex_rate = 2.53405

amount = float(input('Enter amount: '))
currency_input = input('Enter currency to convert: ')
currency_output = input('Enter currency to convert into: ')
output = 0

if currency_input == 'BGN':
    if currency_output == 'USD':
        output = amount/usd_bg_ex_rate
    elif currency_output == 'EUR':
        output = amount / eur_bg_ex_rate
    elif currency_output == 'GBP':
        output = amount / gbp_bg_ex_rate

if currency_input == 'USD':
    if currency_output == 'BGN':
        output = amount * usd_bg_ex_rate
    elif currency_output == 'EUR':
        output = amount * usd_bg_ex_rate
        output = output / eur_bg_ex_rate
    elif currency_output == 'GBP':
        output = amount * usd_bg_ex_rate
        output = output / gbp_bg_ex_rate

if currency_input == 'EUR':
    if currency_output == 'BGN':
        output = amount * eur_bg_ex_rate
    elif currency_output == 'USD':
        output = amount * eur_bg_ex_rate
        output = output / eur_bg_ex_rate
    elif currency_output == 'GBP':
        output = amount * eur_bg_ex_rate
        output = output / gbp_bg_ex_rate

if currency_input == 'GBP':
    if currency_output == 'BGN':
        output = amount * gbp_bg_ex_rate
    elif currency_output == 'USD':
        output = amount * gbp_bg_ex_rate
        output = output / usd_bg_ex_rate
    elif currency_output == 'EUR':
        output = amount * gbp_bg_ex_rate
        output = output / eur_bg_ex_rate


print (f'{output:.2f}')
