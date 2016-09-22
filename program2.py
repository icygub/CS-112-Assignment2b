#This program collects employee data and prints payroll information

print("Enter employee's name: ")
employee = str(input())

print("Enter hours worked this week: ")
hours = int(input())

print("Enter hourly rate of pay: ")
payRate = float(input())

print("Enter federal tax rate: ")
fRate = float(input())

print("Enter state tax rate: ")
sRate = float(input())

grossPay = "%.2f" % (hours * payRate)

print("\nEmployee name:",employee)
print("Hours:        ",hours)
print("Pay Rate:      $" + str(payRate))
print("Gross Pay:     $" + str(grossPay))
print("Deductions:")

fWithholding = "%.2f" % (float(grossPay) * fRate)
print("\tFederal Withholding: $" + str(fWithholding))

sWithholding = "%.2f" % (float(grossPay) * sRate)
print("\tState Withholding:   $" + str(sWithholding))

totalDeductions = "%.2f" % (float(fWithholding) + float(sWithholding))
print("\tTotal Deductions:    $" + str(totalDeductions))

netPay = "%.2f" % (float(grossPay) - float(totalDeductions))
print("Net Pay: $" + str(netPay))



      


