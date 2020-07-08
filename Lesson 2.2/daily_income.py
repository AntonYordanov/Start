working_days_per_month = int(input())
daily_income = float(input())
usd_to_bgn = float (input())
monthly_salary = daily_income*working_days_per_month
annual_income = monthly_salary*12 + monthly_salary*2.5
taxes = annual_income * 0.25
net_yearly_income = (annual_income - taxes)
salary_in_leva = net_yearly_income*usd_to_bgn
print(round(salary_in_leva/365,2))