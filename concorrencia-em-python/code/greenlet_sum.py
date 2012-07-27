import greenlet

total = 0


class GreenSum(greenlet.greenlet):

    def __init__(self, start, end):
        super(GreenSum, self).__init__()
        self.begin = start
        self.end = end

    def run(self):
        global total
        sum = 0
        for n in xrange(self.begin, self.end, 2):
            sum += n
        total += sum

N_GREENS = 5000
increment = 10000000 / N_GREENS
start = 1
for i in range(N_GREENS):
    GreenSum(start, start+increment).switch()
    start += increment
print "Sum is %d" % total
