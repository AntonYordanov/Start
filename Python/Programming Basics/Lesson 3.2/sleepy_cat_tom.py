import math

holidays = int(input())
working_days = 365 - holidays
total_play_minutes = (working_days * 63) + (holidays * 127)
difference = math.fabs(30000 - total_play_minutes)
hours = difference / 60
minutes = difference % 60

if total_play_minutes > 30000:
    print('Tom will run away')
    print(f'{math.floor(hours)} hours and {math.floor(minutes)} minutes for play')
else:
    print('Tom sleeps well')
    print(f'{math.floor(hours)} hours and {math.floor(minutes)} minutes')
    print('less for play')
