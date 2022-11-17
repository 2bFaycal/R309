import time
import multiprocessing

def task ():
    print (f"start for 1 sec")
    time.sleep(1)
    print (f"FINITO")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print (f"FINITO dans {round(end-start, 2)} second(s)")