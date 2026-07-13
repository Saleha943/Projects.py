students={}
while True:
    print("\n1.Add 2.Search 3.Show All 4.Exit")
    c=input("Choice: ")
    if c=="1":
        n=input("Name: ")
        m=float(input("Marks: "))
        students[n]=m
    elif c=="2":
        n=input("Name: ")
        print(students.get(n,"Not found"))
    elif c=="3":
        for n,m in students.items():
            print(n,m)
    elif c=="4":
        break