from flask import Flask, render_template, request
import requests
from classes import CreditRisk



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def data():

        if request.method == 'POST':
            result = 0
            credit_history = request.form.get('creditHistory')
            education = request.form.get('education')
            business_experience = request.form.get('businessExperience')
            management_experience = request.form.get('managementExperience')
            business_plan = request.form.get('businessPlan')
            stock_exchange = request.form.get('stockExchange')
            isin={}
            if stock_exchange == 'Yes':
                r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=AAPL&token=bs7b5tnrh5rbhhsbbkl0')
                isin=r.json()
            loan_amount = float(request.form.get('loanAmount'))
            value_of_asset = float(request.form.get('valueofAsset'))
            current_assets = float(request.form.get('currentAssets'))
            current_liabilities = float(request.form.get('currentLiabilities'))
            net_income = float(request.form.get('netIncome'))
            shareholders_equity = float(request.form.get('shareholdersEquity'))
            total_liabilities = float(request.form.get('totalLiabilities'))
            total_assets = float(request.form.get('totalAssets'))
            net_sales = float(request.form.get('netSales'))
            average_total_assets = float(request.form.get('averageTotalassets'))
            net_profit = float(request.form.get('netProfit'))
            revenue = float(request.form.get('revenue'))

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

           # result = eval(str(first_value + second_value))
            return render_template('index.html', stock_exchange=stock_exchange, result=result, country=isin['country'] if stock_exchange == 'Yes' else '', currency=isin['currency'] if stock_exchange == 'Yes' else '', exchange=isin['exchange'] if stock_exchange == 'Yes' else '', finnhubIndustry=isin['finnhubIndustry'] if stock_exchange == 'Yes' else '', ipo=isin['ipo'] if stock_exchange == 'Yes' else '', marketCapitalization=isin['marketCapitalization'] if stock_exchange == 'Yes' else '', name=isin['name'] if stock_exchange == 'Yes' else '', phone=isin['phone'] if stock_exchange == 'Yes' else '', shareOutstanding=isin['shareOutstanding'] if stock_exchange == 'Yes' else '', ticker=isin['ticker'] if stock_exchange == 'Yes' else '', weburl=isin['weburl'] if stock_exchange == 'Yes' else '')

        elif request.method == 'GET':
            return render_template('index.html')

if __name__ == '__main__':
    app.run()

@app.errorhandler(500)
def page_not_found(e):
    return render_template('index.html', result='Not number/s.')


