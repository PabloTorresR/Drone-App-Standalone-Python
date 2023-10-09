from .app_types import Movement, Position, World
from .history import History
from .utils import MOVEMENTS


class CLI:
    def read_world_bounds(self) -> World:
        while True:
            print("To begin, enter the world bounds: (h, w, d)")
            user_input = input()

            try:
                height, width, depth = map(int, user_input.split())

                if 0 <= height <= 100 and 0 <= width <= 100 and 0 <= depth <= 100:
                    print("=== Volodrone Sensor Data read.")
                    print(f"World: height = {height}, width = {width}, depth = {depth}")
                    return height, width, depth
                else:
                    print("Values must be between 0 and 100 for each dimension.")
            except ValueError:
                print("Invalid input. Please enter three integers separated by spaces.")

    def display_initialising(self) -> None:
        print("=== Volodrone Initialising")

    def display_drone_start_position(self, start_position: Position) -> None:
        print(f"Drone starts at: {start_position}")

    def display_takeoff(self) -> None:
        print("=== Volodrone Take Off")

    def display_movement(
        self, movement: Movement, new_position: Position, total_distance: float
    ) -> None:
        print(f"{movement} -> {new_position} [{total_distance}]")

    def display_landing(self) -> None:
        print("=== Volodrone Landing")

    def read_movement_command(self) -> Movement:
        while True:
            print(
                "Enter a movement direction [LEFT, RIGHT, UP, DOWN, FORWARD, BACKWARD] and distance. Ex: LEFT 3"
            )
            user_input = input()

            try:
                direction, distance = user_input.split()
                direction = direction.upper()

                if direction in MOVEMENTS and distance.isdigit():
                    return tuple(axis * int(distance) for axis in MOVEMENTS[direction])  # type: ignore
                else:
                    print("Invalid input. Please follow the format: DIRECTION DISTANCE")
            except ValueError:
                print("Invalid input. Please follow the format: DIRECTION DISTANCE")

    def display_crash_inminent(self, movement: Movement) -> None:
        print(f"{movement} -> CRASH IMMINENT - AUTOMATIC COURSE CORRECTION")

    def display_history(self, history: History) -> None:
        print("Movements:", history.movements)
        print("Positions:", history.positions)
