import logging

logging.basicConfig(level='INFO')

class Borg:
    """Borg class making class attributes global."""
    _shared_state = {} # State shared by each instance

    def __init__(self) -> None:
        self.__dict__ = self._shared_state # Make it an attribute dictionary
        self.state = None

    def __str__(self) -> str:
        return self.state
        
def main() -> None:
    object_1 = Borg()
    object_2 = Borg()

    object_1.state = "State 1"
    object_2.state = "State 2"

    logging.info(object_1) # >> State 2
    logging.info(object_2) # >> State 2


if __name__ == '__main__':
    main()