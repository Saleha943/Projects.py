passwords={}
while True:
    print("1.Save 2.View 3.Exit")
    c=input("Choice: ")
    if c=="1":
        site=input("Site: ")
        passwords[site]=input("Password: ")
    elif c=="2":
        print(passwords)
    else: break