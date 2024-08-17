# Name: Camille Dana
# ID: 003277157
##
#  This program computes income taxes, using a simplified tax schedule.
#

# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25

tax1 = 0
tax2 = 0
tax3 = 0

# Read income and marital status     
maritalStatus = input("Are you married or single (M or S)?: ")
income = float(input("What is your income?: "))
if maritalStatus == "S":
        if income <= 8000:
               tax1 = RATE1 * income
        elif income > 32000:
                tax3 = 4400 + (income-32000) * RATE3
        else:
                tax2 = 800 + (income-8000) * RATE2
else: 
  if maritalStatus == "M":
        if income <= 16000:
                tax1 = RATE1 * income
        elif income > 64000:
                tax3 = 8800 + (income-64000) * RATE3
        else:
                tax2 = 1600 + (income-16000) * RATE2
totalTax = tax1 + tax2 + tax3
print("Your tax payable is $%.2f" % totalTax)
