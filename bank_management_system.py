balance=0
while True:
    print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
    c=input("Choice: ")
    if c=="1":
        balance+=float(input("Amount: "))
    elif c=="2":
        a=float(input("Amount: "))
        if a<=balance: balance-=a
        else: print("Insufficient funds")
    elif c=="3":
        print(balance)
    else: break