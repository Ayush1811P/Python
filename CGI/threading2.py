import threading as tr
lock=tr.Lock()
def task():
    num=0
    
    print("Program starts")
    for i in range(3):
        num+=1
        print(num)
t1=tr.Thread(target=task) 
t2=tr.Thread(target=task) 
t1.start()
t2.start()