from dataclasses import dataclass

from .app_types import Movement, Position


@dataclass
class Drone:
    """Volodrone class"""

    position: Position

    def move(self, command: Movement) -> Position:
        """Called each time the drone receives the order to move"""
        self.position = tuple(x + y for x, y in zip(self.position, command))  # type: ignore
        return self.position  # type: ignore
