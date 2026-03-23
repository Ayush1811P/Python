tasks=[]
while True:
    print("\n1:Add task\t2: Remove Task\t 3: Display-All")
    try:
        choice=int(input("\tEnter choice: "))
    except ValueError:
        print("\tValue error!")
    try:

        if choice==1:
            ch=1
            while ch==1:
                task=input("\tEnter taks: ")
                tasks.append(task)
                ch=int(input("\twant to add more? || Y=1  N=0 "))
                

        elif choice==2:
            if len(tasks)==0:
                    print(-1)
            rm=1
            while rm==1:
                if len(tasks)==0:
                        print("list empty")
                        break
                else: 
                    remove=input("\tEnter task to remove: ").lower()
                    if remove in tasks:                   
                        tasks.remove(remove)
                        rm=int(input("\twant to remove more? || Y=1  N=0 "))
                    else:
                        print("\tTask not in list to remove!") 
                           
        elif choice==3:
            if len(tasks)==0:
                print("list empty")
            i=1
            for t in tasks:
                print(f"{i}: {t}")
                i+=1
        else:
            print("Enter valid choice")        
    except Exception:
        print(-1)        