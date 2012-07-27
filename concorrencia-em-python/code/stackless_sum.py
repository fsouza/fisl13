import stackless


def sum(ch, begin, end):
    value = 0
    for n in xrange(begin, end, 2):
        value += n
    ch.send(value)

if __name__ == '__main__':
    N_TASKS = 50
    increment = 1000000 / N_TASKS
    start = 1
    ch = stackless.channel()
    for i in range(N_TASKS):
        task = stackless.tasklet(sum)
        task.setup(ch, start, start + increment)
    total = 0
    for i in range(N_TASKS):
        total += ch.receive()
    print "Sum is %d." % total
