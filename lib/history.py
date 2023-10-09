from dataclasses import dataclass, field
from typing import List

from .app_types import Movement, Position
from .utils import calculate_modulus_n_dimension

INITIAL_POSITIONS = []
INITIAL_MOVEMENTS = []


@dataclass
class History:
    """History of the flight"""

    positions: List[Position] = field(default_factory=lambda: INITIAL_POSITIONS)
    movements: List[Movement] = field(default_factory=lambda: INITIAL_MOVEMENTS)

    @property
    def total_distance(self) -> float:
        """Calculates the total distance travelled by the drone"""
        commands_distances = [
            calculate_modulus_n_dimension(vector) for vector in self.movements
        ]

        return sum(commands_distances)

    def update_history(self, new_position: Position, new_movement: Movement) -> None:
        """Adds new position and movement to the history"""
        self.positions.append(new_position)
        self.movements.append(new_movement)
