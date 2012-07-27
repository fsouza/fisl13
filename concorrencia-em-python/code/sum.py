import threading

N_ITEMS = 1000000000
N_THREADS = 4
threads = []
start = 1
increment = N_ITEMS / N_THREADS
while start < increment:
    t = threading.Thread(target=sum, args=[xrange(start, start+increment)])
    t.start()
    threads.append(t)
    start += increment
for t in threads:
    t.join()
