import csp.csp as csp


@csp.process
def sum(ch, begin, end):
    value = 0
    for n in xrange(begin, end, 2):
        value += n
    ch.write(value)

if __name__ == '__main__':
    N_PROCS = 50
    increment = 1000000 / N_PROCS
    start = 1
    ch = csp.Channel()
    for i in range(N_PROCS):
        proc = sum(ch, start, start + increment)
        proc.start()
    total = 0
    for i in range(N_PROCS):
        total += ch.read()
    print "Sum is %d." % total
