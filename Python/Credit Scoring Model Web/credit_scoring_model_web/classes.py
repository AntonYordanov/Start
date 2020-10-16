class CreditRisk:
    def __init__(self, credit_history, education, business_experience, management_experience,
                 business_plan, stock_exchange, loan_amount, value_of_asset,
                 current_assets, current_liabilities, net_income, shareholders_equity,
                 total_liabilities, total_assets, net_sales,
                 average_total_assets, net_profit, revenue):
        self.credit_history = credit_history
        self.education = education
        self.business_experience = business_experience
        self.management_experience = management_experience
        self.business_plan = business_plan
        self.stock_exchange = stock_exchange
        self.loan_amount = float(loan_amount)
        self.value_of_asset = float(value_of_asset)
        self.current_assets = float(current_assets)
        self.current_liabilities = float(current_liabilities)
        self.net_income = float(net_income)
        self.shareholders_equity = float(shareholders_equity)
        self.total_liabilities = float(total_liabilities)
        self.total_assets = float(total_assets)
        self.net_sales = float(net_sales)
        self.average_total_assets = float(average_total_assets)
        self.net_profit = float(net_profit)
        self.revenue = revenue

    def check_credit_history(self, result):
        if (self.credit_history == 'Good'):
            return result + 10
        elif (self.credit_history == 'Bad'):
            return result - 10

    def check_education(self, result):
        if (self.education == 'Master degree'):
            return result + 10
        elif (self.education == 'Bachelor degree'):
            return result + 8
        elif (self.education == 'High school'):
            return result + 5
        elif (self.education == 'No education'):
            return result

    def check_business_experience(self, result):
        if (self.business_experience == 'More_than_10_years'):
            return result + 10
        elif (self.business_experience == 'More_than_5_years'):
            return result + 8
        elif (self.business_experience == 'More_than_3_years'):
            return result + 5
        elif (self.business_experience == 'No_business_experience'):
            return result

    def check_management_experience(self, result):
        if (self.management_experience == 'More_than_10_years'):
            return result + 10
        elif (self.management_experience == 'More_than_5_years'):
            return result + 8
        elif (self.management_experience == 'More_than_3_years'):
            return result + 5
        elif (self.management_experience == 'No_management_experience'):
            return result

    def check_business_plan(self, result):
        if (self.business_plan == 'Yes'):
            return result + 10
        elif (self.business_plan == 'No'):
            return result

    def check_stock_exchange(self, result):
        if (self.stock_exchange == 'Yes'):
            return result + 10
        elif (self.stock_exchange == 'No'):
            return result

    def check_loan_to_value(self, result):
        loan_to_value = self.loan_amount / self.value_of_asset
        if (loan_to_value <= 1):
            return result + 10
        elif (loan_to_value > 1):
            return result + 5

    def check_current_ratio(self, result):
        current_ratio = self.current_assets / self.current_liabilities
        if (current_ratio >= 1.2):
            return result + 10
        elif (current_ratio < 1.2):
            return result

    def check_return_on_equity(self, result):
        return_on_equity = self.net_income / self.shareholders_equity
        if (return_on_equity >= 14):
            return result + 10
        elif (return_on_equity < 10):
            return result + 5

    def check_debt_ratio(self, result):
        debt_ratio = self.total_liabilities / self.total_assets
        if (debt_ratio >= 33):
            return result + 10
        elif (debt_ratio < 100):
            return result

    def check_asset_turnover_ratio(self, result):
        asset_turnover_ratio = self.net_sales / self.average_total_assets
        if (asset_turnover_ratio >= 100):
            return result + 10
        elif (asset_turnover_ratio < 50):
            return result

    def check_net_profit_margin(self, result):
        net_profit_margin = self.net_profit / self.revenue
        if (net_profit_margin >= 20):
            return result + 10
        elif (net_profit_margin < 5):
            return result + 5

    def get_result(self, result):
        if result > 90:
            return 'Credit Rating_A'
        elif result > 70:
            return 'Credit Rating_B'
        elif result <= 70:
            return 'Credit Rating_C'
