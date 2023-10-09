from lib.cli import CLI
from lib.drone import Drone
from lib.flight import Flight
from lib.history import History
from lib.utils import random_tuple_n_dimension

N_COMMANDS = 6


def main() -> None:
    cli = CLI()
    cli.display_initialising()
    world = cli.read_world_bounds()
    drone_starting_position = random_tuple_n_dimension(
        *world
    )  # World dimensions bound the posible positions for the drone
    drone = Drone(drone_starting_position)  # type: ignore
    history = History()
    flight = Flight(world, drone, cli, history)
    flight.play(N_COMMANDS)


if __name__ == "__main__":
    main()
