import math

year_type = input()
vacation_days_count = int(input())
weekends_in_hometown = int(input())

total_games_played = 0

weekends_in_sofia = 48 - weekends_in_hometown

total_games_played = 3 / 4 * (weekends_in_sofia)
total_games_played += 2 / 3 * vacation_days_count
total_games_played += weekends_in_hometown

if year_type == 'normal':
    print(math.floor(total_games_played))
elif year_type == 'leap':
    total_games_played += 0.15 * total_games_played
    print(math.floor(total_games_played))
