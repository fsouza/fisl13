from concurrent import futures


def sum(start, end):
    value = 0
    for n in range(start, end, 2):
        value += n
    return value

if __name__ == '__main__':
    N_WORKERS = 10
    increment = 1000000 // N_WORKERS
    start = 1
    begins = []
    ends = []
    for i in range(N_WORKERS):
        begins.append(start)
        ends.append(start + increment)
        start += increment
    with futures.ProcessPoolExecutor(max_workers=N_WORKERS) as executor:
        values = executor.map(sum, begins, ends)
        result = 0
        for v in values:
            result += v
        print("Sum is %d" % result)
