n = int(input())

positive_nums = []
negative_nums = []

for iteration in range(n):
    current_num = int(input())
    if current_num < 0:
        negative_nums.append(current_num)
    else:
        positive_nums.append(current_num)

print(positive_nums)
print(negative_nums)

result = 0

for el in negative_nums:
    result += el

print(f'Count of positives: {len(positive_nums)}. '
      f'Sum of negatives: {result}')