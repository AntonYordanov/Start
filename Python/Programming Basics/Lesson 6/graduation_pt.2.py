name = input()
year = 1
is_flanked = False
grades_sum = 0

while year <= 12:
    yearly_grade = float(input())

    if yearly_grade < 4:

        if is_flanked:
            break

        is_flanked = True
        continue

    grades_sum += yearly_grade
    year += 1

if year <= 12:
    print(f'{name} has been excluded at {year} grade')
else:
    print(f'{name} graduated. Average grade: {grades_sum / 12:.2f}')