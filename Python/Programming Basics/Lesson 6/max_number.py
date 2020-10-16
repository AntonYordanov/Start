max_number = int(input())

line = input()
while line !='Stop':
    current_number = int(line)

    if current_number > max_number:
        max_number = current_number

    line = input()

print(max_number)