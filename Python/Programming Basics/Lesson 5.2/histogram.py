n = int(input())

p1_percentage = 0
p2_percentage = 0
p3_percentage = 0
p4_percentage = 0
p5_percentage = 0

cnt_p1 = 0
cnt_p2 = 0
cnt_p3 = 0
cnt_p4 = 0
cnt_p5 = 0

for index in range(n):
    current_number = int(input())

    if current_number < 200:
        cnt_p1 += 1
    elif 200 <= current_number <= 399:
        cnt_p2 += 1
    elif 400 <= current_number <= 599:
        cnt_p3 += 1
    elif 600 <= current_number <= 799:
        cnt_p4 += 1
    else:
        cnt_p5 += 1

p1_percentage = cnt_p1 * 100 / n
p2_percentage = cnt_p2 * 100 / n
p3_percentage = cnt_p3 * 100 / n
p4_percentage = cnt_p4 * 100 / n
p5_percentage = cnt_p5 * 100 / n

print('%.2f' % p1_percentage + '%')
print('%.2f' % p2_percentage + '%')
print('%.2f' % p3_percentage + '%')
print('%.2f' % p4_percentage + '%')
print('%.2f' % p5_percentage + '%')
