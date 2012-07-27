import threading

total = 0
mutex = threading.Lock()


class DumbestSum(threading.Thread):

    def __init__(self, start, end):
        super(DumbestSum, self).__init__()
        self.begin = start
        self.end = end

    def run(self):
        global total
        for n in xrange(self.begin, self.end, 2):
            mutex.acquire()
            total += n
            mutex.release()

threads = []
increment = 1000000 / 4
start = 1
for i in range(4):
    t = DumbestSum(start, start+increment)
    t.start()
    start += increment
    threads.append(t)

for t in threads:
    t.join()
print "The sum is %d." % total
