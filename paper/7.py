def Cal_Interest(accBalance, interestRate):
    totalInterest = accBalance * interestRate / 100
    return totalInterest




def Display_details(accHolderName, accHoldAccNo, accType, accBalance, interestRate, totalInterest):
    print("--Account Details--")
    print("Account holder name: ", accHolderName)
    print("Account number: ", accHoldAccNo)
    print("Account type: ", accType)
    print("Current Interest rate: ", interestRate)
    print("")
    print("Account balance: ", accBalance)
    print("Interest Earned: ", totalInterest)

accHolderName = str(input("Enter the account holder name: "))
accHoldAccNo = int(input("Enter the account number: "))
accType = str(input("Enter the account type: 1. Cureent 2. Savings: "))
if accType == "1":
    accType = "Current"
elif accType == "2":
    accType = "Savings"
else:
    print("Invalid account type")
    exit()
accBalance = int(input("Enter the account balance: "))
if accBalance < 0:
    print("Invalid account balance")
    exit()
interestRate = float(input("Enter the interest rate: "))
if interestRate < 0:
    print("Invalid interest rate")
    exit()
else:
    totalInterest = Cal_Interest(accBalance, interestRate)
    netAmount = accBalance + totalInterest
    Display_details(accHolderName, accHoldAccNo, accType, accBalance, interestRate, totalInterest)