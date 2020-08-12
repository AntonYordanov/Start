kids_tickets = 0
student_tickets = 0
standard_tickets = 0

movie_name = input()
while movie_name != 'Finish':
    empty_spaces = int(input())
    bought_tickets = 0

    ticket_type = input()
    while ticket_type != 'End':
        bought_tickets += 1

        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == 'student':
            student_tickets += 1
        else:
            kids_tickets += 1

        if bought_tickets == empty_spaces:
            break

        ticket_type = input()

    percentage_full = bought_tickets / empty_spaces * 100
    print(f'{movie_name} - {percentage_full:.2f}% full.')

    movie_name = input()

total_tickets = kids_tickets + student_tickets + standard_tickets
print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kids_tickets / total_tickets * 100:.2f}% kids tickets.')