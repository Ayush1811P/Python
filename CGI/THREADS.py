import threading as tr
import time
def task1(num):
    for i in range(num):
        print("Task 1 is running")
        time.sleep(0.1)

def task2(num2):
    for i in range(num2):
        print("Task 2 is running")
        time.sleep(0.1)


# print(t.task1())

# print(t.taks2())            

thread1=tr.Thread(target=task1,args=(5,))
thread2=tr.Thread(target=task2,args=(5,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()