import multiprocessing


def sum(q, start, end):
    value = 0
    for n in xrange(start, end, 2):
        value += n
    q.put(value)

N_PROCS = 8
procs = []
increment = 1000000 / N_PROCS
start = 1
values = multiprocessing.Queue()

for i in range(N_PROCS):
    p = multiprocessing.Process(target=sum, args=(values, start, start + increment))
    p.start()
    start += increment
    procs.append(p)

for p in procs:
    p.join()

total = 0
while not values.empty():
    total += values.get()
print "The sum is %d." % total
