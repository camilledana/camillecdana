# Calculate Tip and Pmt each friend pays.

n=6 # Number friends splitting bill
m=12043 # Bill including taxes
l=0.20 # Tip Percentage
b=(m*l)/n # Total cost per person
print(b)

# Calculate compounding interest per year.

P=2000
r=0.08
t=int(input('Enter number of year: '))
balance=P*(1+r*t)
print(balance)
