def Discount_Cal(totAmount):
    if totAmount <= 2500:
        discount = totAmount * (5/100)
    elif totAmount <= 5000 and totAmount > 2500:
        discount = totAmount * (10/100)
    else:
        discount = totAmount * (15/100)
    return discount


amount = float(input("Enter the amount: "))
discount = Discount_Cal(amount)
print("Discount: ", discount)
print("Net Pay: ", amount - discount)
