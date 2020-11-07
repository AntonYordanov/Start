numbers_of_electrons = int(input())

electrons = []
cell_number = 1

while numbers_of_electrons > 0:
    possible_of_electrons = 2*cell_number**2
    if possible_of_electrons > numbers_of_electrons:
        electrons.append(numbers_of_electrons)
    else:
        electrons.append(possible_of_electrons)
    numbers_of_electrons -= possible_of_electrons
    cell_number += 1

print(electrons)