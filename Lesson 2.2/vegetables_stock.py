vegetables_price = float(input())
fruits_price = float(input())
vegetables_quantity = int (input())
fruits_quantity = int (input())
def string_to_number(str):
  if("." in str):
    try:
      res = float(str)
    except:
      res = str
  elif(str.isdigit()):
    res = int(str)
  else:
    res = str
  return(res)
vegetables_total_price = vegetables_price * vegetables_quantity
fruits_total_price = fruits_price * fruits_quantity
print ((vegetables_total_price + fruits_total_price) / 1.94)