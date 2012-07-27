# -*- coding: utf-8 -*-
import time

import csp.csp as csp


def transport(passenger):
    print "Transporting %s..." % passenger,
    time.sleep(2)
    print "ok"


@csp.process
def elevator(chan):
    while True:
        transport(chan.read())


@csp.process
def people(chan, names):
    for name in names:
        chan.write(name)
    chan.poison()


if __name__ == '__main__':
    names = ["Francisco", "Chico", "Xikin", "Maria", "José", "Pedro", "João"]
    chan = csp.Channel()
    csp.Par(elevator(chan), elevator(chan), elevator(chan), people(chan, names)).start()
