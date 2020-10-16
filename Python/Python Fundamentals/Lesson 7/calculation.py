def simple_calculation(operator, num_1, num_2):
    if operator == 'multiply':
        return num_1 * num_2
    elif operator == 'divide':
        return num_1 // num_2
    elif operator == 'add':
        return num_1 + num_2
    elif operator == 'subtract':
        return num_1 - num_2


operator = input()
num_1 = int(input())
num_2 = int(input())
print(simple_calculation(operator, num_1, num_2))
