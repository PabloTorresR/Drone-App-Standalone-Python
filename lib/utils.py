"""Utils functions for the different classes"""
import math
import random
from typing import Tuple, Union


def random_tuple_n_dimension(*max_dimensions: int) -> Tuple[int, ...]:
    """
    Generate a random tuple within specified maximum dimensions.

    Args:
        *max_dimensions (int): The maximum values for each coordinate (X, Y, Z, and more, or less).

    Returns:
        Tuple[int, ...]: A random tuple with the specified dimensions.
    """
    random_values = [random.randint(0, max_dim) for max_dim in max_dimensions]
    return tuple(random_values)


def calculate_modulus_n_dimension(vector: Tuple[Union[float, int], ...]) -> float:
    """
    Calculate the modulus of an N-dimensional tuple representing a vector.

    Args:
        vector (Tuple[Union[float, int], ...]): The N-dimensional vector.

    Returns:
        float: The modulus of the vector.
    """
    sum_of_squares = sum(component**2 for component in vector)

    modulus = math.sqrt(sum_of_squares)
    return modulus


MOVEMENTS = {
    "LEFT": (-1, 0, 0),
    "RIGHT": (1, 0, 0),
    "UP": (0, 0, 1),
    "DOWN": (0, 0, -1),
    "FORWARD": (0, 1, 0),
    "BACKWARD": (0, -1, 0),
}
