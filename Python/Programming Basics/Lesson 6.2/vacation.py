money_needed = float(input())
available_money = float(input())

spend_count = 0
total_days_count = 0

while available_money < money_needed:
    command = input()
    command_money = float(input())

    if command == 'spend':
        spend_count += 1
        total_days_count += 1

        if available_money < command_money:
            available_money = 0
        else:
            available_money -= command_money

        if spend_count == 5:
            print('You can\'t save the money.')
            print(total_days_count)
            break

    elif command == 'save':
        spend_count = 0
        available_money += command_money
        total_days_count += 1

if available_money >= money_needed:
    print(F'You saved the money for {total_days_count} days.')
