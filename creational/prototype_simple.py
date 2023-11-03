import logging
import copy

logging.basicConfig(level='INFO')

class Prototype:
    """A basic Prototype class."""
    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name: str, obj: object) -> None:
        """Register an object."""
        self._objects[name] = obj
    
    def unregister_object(self, name: str) -> None:
        """Unregister an object."""
        del self._objects[name]
    
    def clone(self, name, **attr) -> None:
        """Clone a registered object and update its attributes."""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    """A simple Car class."""
    def __init__(self) -> None:
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
    
    def __str__(self) -> str:
        return f'{self.name} | {self.color} | {self.options}'

def main() -> None:
    car_1 = Car()
    prototype = Prototype()
    prototype.register_object("Skylark", car_1)

    car_2 = prototype.clone("Skylark")
    logging.info(car_2)


if __name__ == '__main__':
    main()