book_count = 0
favorite_book_name = input()

while True:
    current_book = input()

    if current_book == favorite_book_name:
        print(f'You checked {book_count} books and found it.')
        break

    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_count} books.')
        break

    book_count += 1