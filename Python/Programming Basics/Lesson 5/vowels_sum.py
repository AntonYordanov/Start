text = input()
total_sum = 0
text = text.lower()

for index in range(0, len(text)):
    symbol = text[index]
    if symbol == 'a':
        total_sum += 1
    elif symbol == 'e':
        total_sum += 2
    elif symbol == 'i':
        total_sum += 3
    elif symbol == 'o':
        total_sum += 4
    elif symbol == 'u':
        total_sum += 5

print(total_sum)
