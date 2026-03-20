tasks=[]#global list
def add_task():
    try:
            task=input("Add task: ")
            tasks.append(task)
    except ValueError:
        print(-1)

def remove_task():
    if len(tasks)==0:
        print("no tasks exist")
    try:
        rm=1
        while rm==1:
            removes=input("Enter task to remove: ")          
            tasks.remove(removes)
            rm=int(input("want to remove more |Y=1  N=0: "))
        
    except ValueError:
        print(-1)
def display():
    if len(tasks)==0:
        print("tasks list is empty")
    i=1    
    for t in tasks:
        print(f"{i}: {t}")
        i+=1

def main():
    while True:
        try:
            print("1:Add task\t2: Remove Task\t 3: Display-All")
            choice=int(input("Enter choice: "))
        except ValueError:
            print("Value error!")
        if choice==1:
            ch=1
            while ch==1:    
                add_task()
                ch=int(input("\twant to add more |Y=1  N=0: "))
        elif choice==2:
            remove_task()
        elif choice==3:
            display()
        else:
            print(-1)        

main()            
