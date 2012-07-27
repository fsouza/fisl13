import threading

total = 0
mutex = threading.Lock()


class LocalSum(threading.Thread):

    def __init__(self, start, end):
        super(LocalSum, self).__init__()
        self.begin = start
        self.end = end

    def run(self):
        global total
        tls = threading.local()
        tls.total = 0
        for n in xrange(self.begin, self.end, 2):
            tls.total += n
        mutex.acquire()
        total += tls.total
        mutex.release()

if __name__ == '__main__':
    threads = []
    increment = 1000000 / 4
    start = 1
    for i in range(4):
        t = LocalSum(start, start+increment)
        t.start()
        start += increment
        threads.append(t)

    for t in threads:
        t.join()
    print "The sum is %d." % total
