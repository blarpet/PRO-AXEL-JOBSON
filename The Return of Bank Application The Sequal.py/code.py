
loop = True
balance = []
change = []
deposit = 0
withdrawal = 0


r = open("money.txt", "r")

accountValue = r.read()
r.close

#intValue = int(accountValue)
accountValue = int(accountValue)
#print(type(accountValue))

newAccountSetup = str(input("Is this your first time using this program?[y/n]"))
if newAccountSetup == "y":
    accountValue = 1000
    b = open("balance.txt", "a")
    b.truncate(0)
    b.close
    c = open("change.txt", "a")
    c.truncate(0)
    c.close
while loop == True:
    editAccountValue = str(input("Do you wish to edit the value of your account?[y/n]"))
    if editAccountValue == "y":
        withdrawalOrDeposit = str(input("Do you want to make a withdrawal or a deposit?[withdrawal/deposit]"))
        if withdrawalOrDeposit == "deposit":
            deposit = int(input("How much do you wish to deposit into your account?"))
            if deposit >= 0:
                accountValue = accountValue + deposit
            elif deposit < 0: 
                print("ERROR")
        if withdrawalOrDeposit == "withdrawal" and accountValue > 0:
            withdrawal = int(input("How much do you wish to withdrawal from your account?"))
            if withdrawal >= 0:
                accountValue = accountValue - withdrawal
            elif withdrawal < 0: 
                print("ERROR")
        if withdrawalOrDeposit == "withdrawal" and accountValue <= 0:
            print("You cannot withdraw anything from your account due to your account being empty or you withdrew enough money for it to become empty")
            depositQuestion = str(input("Since your account is empty would you like to make a deposit?[y/n]"))
            if depositQuestion == "y":  
                deposit = int(input("How much do you wish to deposit into your account?"))
                accountValue += deposit
    if editAccountValue == "n":
        loop = False

valueChange = deposit - withdrawal
change.append(valueChange)
c = open("change.txt", "a")
c.write(str(change))
c.close

balance.append(accountValue)
b = open("balance.txt", "a")
b.write(str(balance))
b.close


f = open("money.txt", "a")
f.truncate(0)
f.write(str(accountValue))

dataQuestion = str(input("Do you wish to you see your balance history?[y/n]"))
if dataQuestion == "y":
    b = open("balance.txt", "r")
    print(b.read())
    b.close

dataQuestion2 = str(input("Do you wish to you see your money exchange history?[y/n]"))
if dataQuestion == "y":
    c = open("change.txt", "r")
    print(c.read())
    c.close

f.close