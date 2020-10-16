
from classes import CreditRisk

result = 0

credit_history = input()
education = input()
business_experience = input()
management_experience = input()
business_plan = input()
stock_exchange = input()
loan_amount = float(input())
value_of_asset = float(input())
current_assets = float(input())
current_liabilities = float(input())
net_income = float(input())
shareholders_equity = float(input())
total_liabilities = float(input())
total_assets = float(input())
net_sales = float(input())
average_total_assets = float(input())
net_profit = float(input())
revenue = float(input())

creditRisk = CreditRisk(credit_history, education, business_experience, management_experience,
                        business_plan, stock_exchange, loan_amount, value_of_asset,
                        current_assets, current_liabilities, net_income, shareholders_equity,
                        total_liabilities, total_assets, net_sales,
                        average_total_assets, net_profit, revenue)

result = creditRisk.check_credit_history(result)
result = creditRisk.check_education(result)
result = creditRisk.check_business_experience(result)
result = creditRisk.check_management_experience(result)
result = creditRisk.check_business_plan(result)
result = creditRisk.check_stock_exchange(result)
result = creditRisk.check_loan_to_value(result)
result = creditRisk.check_current_ratio(result)
result = creditRisk.check_return_on_equity(result)
result = creditRisk.check_debt_ratio(result)
result = creditRisk.check_asset_turnover_ratio(result)
result = creditRisk.check_net_profit_margin(result)
result = creditRisk.get_result(result)

print(result)
