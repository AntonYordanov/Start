days_count = int (input())
bakers_count = int (input())
cakes_count = int (input())
waffles_count = int (input())
crepes_count = int (input())
cakes_price = 45
waffles_price = 5.8
crepes_price = 3.2
daily_wage = (cakes_count*cakes_price*waffles_count*waffles_price + cakes_count*crepes_price)*bakers_count
total_sum = daily_wage*days_count
charity_money = total_sum-1.8*total_sum
print(charity_money)