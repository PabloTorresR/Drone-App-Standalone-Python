import unittest
from unittest.mock import MagicMock
from lib.history import History
from lib.drone import Drone
from lib.exceptions import CrashException
from lib.controller import Controller
from lib.app_types import Movement
from lib.cli import CLI
from lib.flight import Flight


class TestFlight(unittest.TestCase):
    def setUp(self):
        # Create mock objects for dependencies
        self.world = (10, 10, 10)
        starting_position = (0, 0, 0)
        self.drone = Drone(starting_position)
        self.controller = CLI()
        self.history = History()

    def test_is_command_possible_valid_command(self):
        flight = Flight(self.world, self.drone, self.controller, self.history)
        valid_command = (1, 0, 0)
        self.assertTrue(flight.__is_command_possible__(valid_command))

    def test_is_command_possible_invalid_command(self):
        flight = Flight(self.world, self.drone, self.controller, self.history)
        invalid_command = (11, 0, 0)
        self.assertFalse(flight.__is_command_possible__(invalid_command))

    def test_history(self):
        flight = Flight(self.world, self.drone, self.controller, self.history)
        valid_command = (1, 0, 0)
        self.assertFalse(self.history.positions)  # Ensure history is initially empty
        self.assertFalse(self.history.movements)  # Ensure history is initially empty
        flight.__send_move_command__(valid_command)
        self.assertTrue(self.history.positions)  # Check that history has been updated
        self.assertTrue(self.history.movements)  # Check that history has been updated

    def test_send_move_command_invalid_command_raises_crash(self):
        flight = Flight(self.world, self.drone, self.controller, self.history)
        invalid_command = (11, 0, 0)
        with self.assertRaises(CrashException):
            flight.__send_move_command__(invalid_command)
