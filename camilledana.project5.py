#Camille Dana


user=input('Please enter employee name: ')
hrpay=float(input('hourly wage in dollars: '))
hrperweek=float(input('hours worked per week: '))
if hrperweek <= 40:
    basepay= round(hrpay*hrperweek,2)
    overtime=0
else:
    basepay=round(40*hrpay, 2)
    overtime=round((hrperweek-40)*(1.5*hrpay), 2)

grosspay=basepay+overtime

print("Employee Name: " + user)
print("Base Pay: $" + str(basepay))
print("Overtime: $" + str(overtime))
print("Gross Pay: $" + str(grosspay))


