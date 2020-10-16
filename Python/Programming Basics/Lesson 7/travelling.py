while True:
    destination = input()

    if destination == 'End':
        break

    money_needed = int(input())
    budget = 0
    while budget < money_needed:
        budget += int(input())

    print(f'Going to {destination}!')


