# Name: Camille Dana
# ID: 003277157
##
#This program replicates a bank ATM machine.
#

checking=1450.0
savings=10.0
pin=4321

userInput = int(input('Enter pin number(4 digit number):'))
if userInput == 4321:
    account = input('Please enter "s" for savings and "c" for checking:   ')
    if account == "s":
        print(savings)
    else:
        print(checking)
else:
    userInput = int(input('Enter pin number(4 digit number):'))
    if userInput == 4321:
        account = input('Please enter "s" for savings and "c" for checking:   ')
        if account == "s":
            print(savings)
        else:
            print(checking)
    else:
        userInput = int(input('Enter pin number(4 digit number):'))
        if userInput == 4321:
            account = input('Please enter "s" for savings and "c" for checking:   ')
            if account == "s":
                print(savings)
            else:
                print(checking)
        else:
            print('Your Password is blocked.')

#
     # if userInput == 4321:
     #    userInput=int(input('Enter pin number(4 digit number):'))
     #    account = input('Please enter "s" for savings and "c" for checking')
     #    if userInput == str("s"):
     #        print(savings)
     #    elif userInput == str("c"):
     #        print(checking)
     #        #break
     #    else:
     #            print('Incorrect Password')

                # print('\nYour Password is blocked.')
























