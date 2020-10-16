deposit_sum = float (input())
duration = int (input())
yearly_percentage = float (input())
interest = deposit_sum * (yearly_percentage / 100)
interest_per_month = interest / 12
result_sum = deposit_sum + duration * interest_per_month
print(result_sum)

