import math

amount_of_biscuits = int(input())
count_of_the_workers = int(input())
amount_of_biscuits_2 = int(input())

count_buscuits = 20 * amount_of_biscuits * count_of_the_workers + 10 * amount_of_biscuits * count_of_the_workers * 0.75

count_buscuits = math.floor(count_buscuits)
print(f'You have produced {count_buscuits} biscuits for the past month.')
if count_buscuits  > amount_of_biscuits_2:

    the_bigest = ((count_buscuits - amount_of_biscuits_2)/amount_of_biscuits_2) * 100
    print(f'You produce {the_bigest:.2f} percent more biscuits.')
else:
    the_bigest = ((amount_of_biscuits_2- count_buscuits )/amount_of_biscuits_2) * 100
    print(f'You produce {the_bigest:.2f} percent less biscuits.')