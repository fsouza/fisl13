# -*- coding: utf-8 -*-
import time

import csp.csp as csp


@csp.process
def elevator(chan):
    while True:
        print "Transporting %s" % chan.read()
        time.sleep(2)


@csp.process
def people(chan, names):
    for name in names:
        chan.write(name)
    chan.poison()

if __name__ == "__main__":
    names = ["Francisco", "Chico", "Maria", "José"]
    chan = csp.Channel()
    csp.Par(elevator(chan), elevator(chan), elevator(chan), people(chan, names)).start()
