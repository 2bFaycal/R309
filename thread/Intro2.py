import threading
import time

def task (i):
    print("Task {i} started")
    time.sleep(1)
    print("Task {i} finished")


start = time.perf_counter()

t1 = threading.Thread(target=task, args=[1])
t1.start()

t2 = threading.Thread(target=task, args=[2])
t2.start()

t1.join()
t2.join()

end = time.perf_counter()
print (f"Finished in {round(end-start, 2)} second(s)")