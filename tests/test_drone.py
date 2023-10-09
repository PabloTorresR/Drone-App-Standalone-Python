import unittest
from lib.drone import Drone


class TestDrone(unittest.TestCase):
    def setUp(self):
        # Initialize a Drone instance with a starting position
        self.starting_position = (0, 0, 0)
        self.drone = Drone(position=self.starting_position)

    def test_initial_position(self):
        self.assertEqual(self.drone.position, self.starting_position)

    def test_move_left(self):
        command = (-1, 0, 0)
        expected_position = (-1, 0, 0)
        self.assertEqual(self.drone.move(command), expected_position)

    def test_move_right(self):
        command = (1, 0, 0)
        expected_position = (1, 0, 0)
        self.assertEqual(self.drone.move(command), expected_position)

    def test_move_up(self):
        command = (0, 0, 1)
        expected_position = (0, 0, 1)
        self.assertEqual(self.drone.move(command), expected_position)

    def test_move_down(self):
        command = (0, 0, -1)
        expected_position = (0, 0, -1)
        self.assertEqual(self.drone.move(command), expected_position)

    def test_move_complex(self):
        # Test a complex movement command
        command = (2, -3, 1)
        expected_position = (2, -3, 1)
        self.assertEqual(self.drone.move(command), expected_position)
