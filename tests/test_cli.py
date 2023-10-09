import unittest
from unittest.mock import patch
from lib.cli import CLI


class TestCLI(unittest.TestCase):
    def test_read_world_bounds_valid_input(self):
        with patch("builtins.input", side_effect=["3 4 5"]):
            cli = CLI()
            world = cli.read_world_bounds()
            self.assertEqual(world, (3, 4, 5))

    def test_read_movement_command_left(self):
        with patch("builtins.input", side_effect=["LEFT 3"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (-3, 0, 0))

    def test_read_movement_command_right(self):
        with patch("builtins.input", side_effect=["RIGHT 2"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (2, 0, 0))

    def test_read_movement_command_up(self):
        with patch("builtins.input", side_effect=["UP 4"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (0, 0, 4))

    def test_read_movement_command_down(self):
        with patch("builtins.input", side_effect=["DOWN 1"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (0, 0, -1))

    def test_read_movement_command_forward(self):
        with patch("builtins.input", side_effect=["FORWARD 5"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (0, 5, 0))

    def test_read_movement_command_backward(self):
        with patch("builtins.input", side_effect=["BACKWARD 2"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (0, -2, 0))

    def test_read_movement_command_decimal_value(self):
        # NOTE: We provide a final correct value in order to exit the while loop inside read_movement_command
        with patch("builtins.input", side_effect=["LEFT 3.5", "LEFT 2"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (-2, 0, 0))

    def test_read_movement_command_negative_value(self):
        # NOTE: We provide a final correct value in order to exit the while loop inside read_movement_command
        with patch("builtins.input", side_effect=["LEFT -2", "LEFT 2"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (-2, 0, 0))

    def test_read_movement_command_invalid_direction(self):
        # NOTE: We provide a final correct value in order to exit the while loop inside read_movement_command
        with patch("builtins.input", side_effect=["DIAGONAL 3", "LEFT 2"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (-2, 0, 0))

    def test_read_movement_command_invalid_characters(self):
        # NOTE: We provide a final correct value in order to exit the while loop inside read_movement_command
        with patch("builtins.input", side_effect=["LEFT abc", "LEFT 2"]):
            cli = CLI()
            movement = cli.read_movement_command()
            self.assertEqual(movement, (-2, 0, 0))

    def test_read_movement_command_case_insensitive(self):
        with patch("builtins.input", side_effect=["left 3", "RIGHT 2"]):
            cli = CLI()
            movement_1 = cli.read_movement_command()
            movement_2 = cli.read_movement_command()

            self.assertEqual(movement_1, (-3, 0, 0))
            self.assertEqual(movement_2, (2, 0, 0))
