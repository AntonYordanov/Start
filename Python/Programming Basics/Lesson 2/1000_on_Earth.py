from datetime import datetime, timedelta

datevalue = input()
dt_object1 = datetime.strptime(datevalue, "%d-%m-%Y")
future_date_after_1000 = dt_object1 + \
                        timedelta(days = 999)
print(future_date_after_1000.strftime("%d-%m-%Y"))