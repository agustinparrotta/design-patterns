import logging

logging.basicConfig(level="INFO")


class Korean:
    """Korean speaker."""

    def __init__(self) -> None:
        self.name = "Korean"

    def speak_korean(self) -> str:
        return "An-neyong?"


class British:
    """English speaker."""

    def __init__(self) -> None:
        self.name = "British"

    def speak_english(self) -> str:
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method names."""

    def __init__(self, object: object, **adapted_method: dict) -> None:
        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        # For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr: any) -> object:
        return getattr(self._object, attr)


def main() -> None:
    # List to store speaker objects
    objects = []

    korean = Korean()

    british = British()

    # Append the objects to the objects list
    objects.append(Adapter(korean, speak=korean.speak_korean))
    objects.append(Adapter(british, speak=british.speak_english))

    for obj in objects:
        logging.info(f"{obj.name} says {obj.speak()}")


if __name__ == "__main__":
    main()
