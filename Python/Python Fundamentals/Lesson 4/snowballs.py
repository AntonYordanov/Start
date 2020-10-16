n_snowballs = int(input())

max_snowballs_snow = None
max_snowballs_time = None
max_snowballs_quality = None

max_score = - 9999999999

for ball in range(1, n_snowballs + 1):
    snowballs_snow = int(input())
    snowballs_time = int(input())
    snowballs_quality = int(input())

    score = (snowballs_snow / snowballs_time) ** snowballs_quality

    if score > max_score:
        max_score = score
        max_snowballs_snow = snowballs_snow
        max_snowballs_time = snowballs_time
        max_snowballs_quality = snowballs_quality

print(f'{max_snowballs_snow} : {max_snowballs_time} = {int(max_score)} ({max_snowballs_quality})')
