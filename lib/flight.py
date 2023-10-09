from dataclasses import dataclass

from .app_types import Movement, World
from .controller import Controller
from .drone import Drone
from .exceptions import CrashException
from .history import History


@dataclass
class Flight:
    """Flight class"""

    world: World
    drone: Drone
    controller: Controller
    history: History

    def __is_command_possible__(self, command: Movement) -> bool:
        """
        Check if an action is possible based on a position, desired movement, and world boundaries.
        """
        new_position = tuple(sum(x) for x in zip(self.drone.position, command))

        for coord, max_limit in zip(new_position, self.world):
            if coord < 0 or coord > max_limit:
                return False

        return True

    def __send_move_command__(self, command: Movement) -> None:
        """Sends the move command to the drone. First a check for the feasibility of the command is runned"""
        if not self.__is_command_possible__(command):
            raise CrashException

        new_position = self.drone.move(command)
        self.history.update_history(new_position, command)

    def turn(self) -> None:
        movement_command = self.controller.read_movement_command()
        try:
            self.__send_move_command__(movement_command)
            self.controller.display_movement(
                movement_command, self.drone.position, self.history.total_distance
            )

        except CrashException:
            self.controller.display_crash_inminent(movement_command)

    def play(self, max_round: int = 5):
        # display the rules
        self.controller.display_drone_start_position(self.drone.position)
        self.controller.display_takeoff()

        for _ in range(max_round):
            self.turn()

        self.controller.display_landing()
