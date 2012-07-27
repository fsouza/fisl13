import threading
import time

N_THREADS = 4
mutex = threading.Lock()

class StupidThread(threading.Thread):

    def run(self):
        mutex.acquire()
        time.sleep(1)
        mutex.release()

threads = []
for i in range(N_THREADS):
    t = StupidThread()
    t.start()
    threads.append(t)
for t in threads:
    t.join()
