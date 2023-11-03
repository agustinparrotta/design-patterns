import logging

logging.basicConfig(level="INFO")


class Dog:
    """A simple dog class."""

    def speak(self) -> str:
        return "Woof!"

    def __str__(self) -> str:
        return "Dog"


class Cat:
    """A simpe cat class."""

    def speak(self) -> str:
        return "Meow!"

    def __str__(self) -> str:
        return "Cat"


class DogFactory:
    """Concrete Factory."""

    def get_pet(self) -> object:
        """Returns a Dog object."""
        return Dog()

    def get_food(self) -> object:
        """Returns a Dog Food object."""
        return "Dog Food!"


class CatFactory:
    """Concrete Factory."""

    def get_pet(self) -> object:
        """Returns a Cat object."""
        return Cat()

    def get_food(self) -> object:
        """Returns a Cat Food object."""
        return "Cat Food!"


class PetStore:
    """PetStore houses our Abstract Factory."""

    def __init__(self, pet_factory: object = None) -> None:
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self) -> None:
        """Utility method to display the details of the objects returned by the DogFactory and CatFactory."""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        logging.info(f"Our pet is {pet}!")
        logging.info(f"Our pet says hello by {pet.speak()}")
        logging.info(f"Its food is {pet_food}")


def main() -> None:
    # Create a concrete factory, create a pet store housing our Abstract Factory and invoke the utility method

    factory = DogFactory()
    shop = PetStore(factory)
    shop.show_pet()

    factory = CatFactory()
    shop = PetStore(factory)
    shop.show_pet()


if __name__ == "__main__":
    main()
