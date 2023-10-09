from typing import Protocol

from .app_types import Movement, Position
from .history import History


class Controller(Protocol):
    def display_initialising(self) -> None:
        raise NotImplementedError()

    def display_drone_start_position(self, start_position: Position) -> None:
        raise NotImplementedError()

    def display_takeoff(self) -> None:
        raise NotImplementedError()

    def display_movement(
        self, movement: Movement, new_position: Position, total_distance: float
    ) -> None:
        raise NotImplementedError()

    def display_landing(self) -> None:
        raise NotImplementedError()

    def read_movement_command(self) -> Movement:
        raise NotImplementedError()

    def display_crash_inminent(self, movement: Movement) -> None:
        raise NotImplementedError()

    def display_history(self, history: History) -> None:
        raise NotImplementedError()
