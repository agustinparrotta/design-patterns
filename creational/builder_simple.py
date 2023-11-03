import logging

logging.basicConfig(level="INFO")


class Director:
    """A Director class."""

    def __init__(self, builder: object) -> None:
        self._builder = builder

    def construct_car(self) -> None:
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self) -> object:
        return self._builder.car


class Car:
    """Product."""

    def __init__(self) -> None:
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return f"{self.model} | {self.tires} | {self.engine}"


class Builder:
    """Abstract Builder."""

    def __init__(self) -> None:
        self.car = None

    def create_new_car(self) -> None:
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder. Provides parts and tools to work on the parts."""

    def add_model(self) -> None:
        self.car.model = "SkyLark"

    def add_tires(self) -> None:
        self.car.tires = "Regular tires"

    def add_engine(self) -> None:
        self.car.engine = "Turbo engine"


def main() -> None:
    builder = SkyLarkBuilder()
    director = Director(builder)

    director.construct_car()
    car = director.get_car()
    logging.info(car)


if __name__ == "__main__":
    main()
