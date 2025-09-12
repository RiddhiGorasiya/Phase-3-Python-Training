import threading

def print_cube(num):
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    print("Square: {}" .format(num * num))

if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
    
# threading.Thread, join(), start()

import threading
import os 

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    
def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    
if __name__ == "__main__":
        
    print("ID of main process: {}".format(os.getpid()))
    
    print("Main thread name: {}".format(threading.current_thread().name))
    
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    
    t1.start()
    t2.start()
    
    t1.join() 
    t2.join()
    
# Python ThreadPool

import concurrent.futures

def worker():
    print("Worker Thread Running")
    
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

print("Main thread continuing to run...")

# Thread-safe operations

import time 
from concurrent.futures import ThreadPoolExecutor

class BankAccount:
    def __init__(self, blance=0):
        self.balance = blance
        
    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)
            self.balance = new_balance
        else:
            raise ValueError("Insufficient balance")
        
account = BankAccount(1000)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(account.withdraw, 100)
    executor.submit(account.withdraw, 100)
    
print("Final balance: {}".format(account.balance))