#Name: Camille Dana
#ID:003277157

num1 = input("Enter an 8 digit credit card number: ")
sum_odd = 0
for i in range(7,0,-2):
    sum_odd+=int(num1[i])

sum_even = 0
for j in range(6, -1, -2):
    double = int(num1[j])*2
    sum_even+= double //10 + double %10

total = sum_odd + sum_even
if total % 10 == 0:
    print("That number is valid")
else:
    print("That number is invalid")



