from threading import Thread
from multiprocessing import Process
from queue import Queue as Thread_Queue 
from multiprocessing import Queue as Process_Queue

def is_armstrong(n):
    a, t = [], n
    while t:
        a.append(t % 10)
        t //= 10
    k = len(a)
    return sum(x ** k for x in a) == n

def find_armstrong(a, b, q=None):
    res = [x for x in range(a, b) if is_armstrong(x)]
    if q:
        q.put(res)
    return res

def find_by_thread(*ranges):
    q = Thread_Queue()
    workers = []
    for r in ranges:
        a, b = r
        t = Thread(target=find_armstrong, args=(a, b, q))
        t.start()
        workers.append(t)

    res = []
    for _ in range(len(ranges)):
        res.extend(q.get())

    return res

def find_by_process(*ranges):
    q = Process_Queue()
    workers = []
    for r in ranges:
        a, b = r
        t = Process(target=find_armstrong, args=(a, b, q))
        t.start()
        workers.append(t)

    res = []
    for _ in range(len(ranges)):
        res.extend(q.get())

    return res

if __name__ == '__main__':
    import time
    t0 = time.time()
    res = find_by_thread([10000000, 15000000], [15000000, 20000000], 
                         [20000000, 25000000], [25000000, 30000000])
    print(res)
    print(time.time() - t0)