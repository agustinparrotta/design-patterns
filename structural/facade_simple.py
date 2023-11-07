import logging

logging.basicConfig(level='INFO')

class Washing:
    """Subsystem # 1."""
    def wash(self):
        return "Washing..." 
 
class Rinsing:
    """Subsystem # 2."""
    def rinse(self):
        return "Rinsing..."
 
class Spinning:
    """Subsystem # 3."""
    def spin(self):
        return "Spinning..."

class WashingMachine:
    """Facade."""
 
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
 
    def startWashing(self):
        logging.info(self.washing.wash())
        logging.info(self.rinsing.rinse())
        logging.info(self.spinning.spin())


def main() -> None:

    washingMachine = WashingMachine()
    washingMachine.startWashing()


if __name__ == '__main__':
    main()
