import logging
from abc import ABC

logging.basicConfig(level="INFO")


class Command(ABC):
    """Class Dedicated to Command."""

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        pass


class CommandImplementation(Command):
    """Class dedicated to Command Implementation."""

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        self.receiver.perform_action()


class Receiver:
    """Class dedicated to Receiver."""

    def perform_action(self):
        logging.info("Action performed in receiver.")


class Invoker:
    """Class dedicated to Invoker"""

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()


def main():
    """Create Receiver object"""
    receiver = Receiver()
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()


if __name__ == "__main__":
    main()
