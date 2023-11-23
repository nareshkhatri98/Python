cost_price = int(input("Enter the cost price:"))
sell_price = int(input("Enter the selling price:"))

if sell_price > cost_price :
  profit = sell_price - cost_price
  print(" we have gain profit :", +profit)
elif sell_price <cost_price:
  loss  = cost_price - sell_price
  print("we have loss :", +loss)

else :
  print("we have made no profit and no loss")