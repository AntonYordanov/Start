
command = ''

words = []
while command != 'end':
    inputcom=input().split(' ')
    command = inputcom[0]
    if command == 'Chat':
        words.append(inputcom[1])
    elif command == 'Delete':
        if inputcom[1] in words:
            words.remove(inputcom[1])
    elif command == 'Edit':
        index =words.index(inputcom[1])
        words[index] = inputcom[2]
    elif command == 'Pin':
        index = words.index(inputcom[1])
        el= words.pop(index)
        words.append(el)
    elif command == 'Spam':
        for index in range(1, len(inputcom)):
            words.append(inputcom[index])


print('\n'.join(map(str, words)))