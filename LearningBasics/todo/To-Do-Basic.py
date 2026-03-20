tasks=[]
print("1:Add task\t2: Remove Task\t 3: Display-All")

while True:
    choice=int(input("Enter choice: "))
    if choice==1:
        ch=1
        while ch==1:
            task=input("Enter taks: ")
            tasks.append(task)
            ch=int(input("want to add more? || Y=1  N=0"))

    elif choice==2:
        if len(tasks)==0:
                print(-1)
        rm=1
        while rm==1:
            remove=input("Enter task to remove: ")
            if remove in tasks:
                tasks.pop(remove)
                rm=int(input("want to remove more? || Y=1  N=0"))
            else:
                print("Task not in list to remove!")            
    elif choice==3:
        if len(tasks)==0:
            print(-1)
        i=1
        for t in tasks:
            print(f"{1}: {t}")
    else:
        print("Enter valid choice")        