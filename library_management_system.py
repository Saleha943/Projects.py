books=["Python","Math","English"]
while True:
    print("\n1.View 2.Borrow 3.Return 4.Exit")
    c=input("Choice: ")
    if c=="1":
        print(books)
    elif c=="2":
        b=input("Book: ")
        if b in books:
            books.remove(b); print("Borrowed")
    elif c=="3":
        books.append(input("Book: "))
    else:
        break