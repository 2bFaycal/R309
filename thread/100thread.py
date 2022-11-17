import threading
import time

def task (i):
    print(f"Task {i} started")
    time.sleep(1)
    print(f"Task {i} finished")

start = time.perf_counter()

T = []

for i in range(100):
    T.append(threading.Thread(target=task, args=[i,]))
for i in range(len(T)):
    T[i].start()
for i in range(len(T)):
    T[i].join()

end = time.perf_counter()
print (f"Finished in {round(end-start, 2)} second(s)")