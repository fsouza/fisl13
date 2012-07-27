import time
import unittest

import csp.csp as csp
import mock

import elevator


class ElevatorTestCase(unittest.TestCase):

    def test_when_passenger_arrives_should_transport_it(self):
        with mock.patch("elevator.transport") as transport:
            chan = csp.Channel()
            proc = elevator.elevator(chan)
            proc.start()
            chan.write("Francisco")
            chan.poison()
            transport.assert_called_with("Francisco")

    def test_elevator_runs_in_a_loop(self):
        with mock.patch("elevator.transport") as transport:
            chan = csp.Channel()
            proc = elevator.elevator(chan)
            proc.start()
            chan.write("Francisco")
            chan.write("Chico")
            chan.write("Xikin")
            chan.poison()
            self.assertEqual(3, transport.call_count)

    def test_people_should_write_names_to_channel_and_poison_it(self):
        chan = csp.Channel()
        proc = elevator.people(chan, ["Francisco", "Chico"])
        proc.start()
        self.assertEqual("Francisco", chan.read())
        self.assertEqual("Chico", chan.read())
        time.sleep(1)
        self.assertTrue(chan._poisoned)

unittest.main()
