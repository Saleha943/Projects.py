tasks=[]
while True:
    print("\n1.Add Task\n2.View Tasks\n3.Exit")
    c=input("Choose: ")
    if c=="1":
        tasks.append(input("Task: "))
    elif c=="2":
        for i,t in enumerate(tasks,1):
            print(i,t)
    elif c=="3":
        break