print ("Enter the monthly savings amount: ")
monthlyAmount = int(input())

print ("Enter the yearly interest rate: ")
yearlyRate = float(input()) * .01 #Percentage converter (e.g. 5 = .05)

monthlyRate = yearlyRate / 12

accountBalance = monthlyAmount
month = 1
while month < 7:
    
    accountBalance *= (1 + monthlyRate)
    month += 1
    if month < 7:
        accountBalance += monthlyAmount

print ("After 6 months the account balance is: ",accountBalance)    
