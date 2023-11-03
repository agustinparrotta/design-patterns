import logging

logging.basicConfig(level="INFO")


class Borg:
    """Borg class making class attributes global."""

    _shared_state = {}  # State shared by each instance

    def __init__(self) -> None:
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):
    """This class now shares all its attributes among its various instances."""

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self._shared_state.update(
            kwargs
        )  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self) -> str:
        return str(self._shared_state)  # Returns the attribute dictionary for printing


def main() -> None:
    # Create a Singleton object and add our first acronym
    x = Singleton(HTTP="Hyper Text Transfer Protocol")
    logging.info(x)

    # Create another singleton object and if it refers to the same attribute dictionary by adding another acronym
    y = Singleton(REST="Representational State Transfer")
    logging.info(y)


if __name__ == "__main__":
    main()
