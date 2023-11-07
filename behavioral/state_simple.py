
import logging

logging.basicConfig(level='INFO')


class State:
    """Base state. This is to share functionality."""
  
    def scan(self):
        # Scan the dial to the next station
        self.pos += 1
  
        # Check for the last station
        if self.pos == len(self.stations):
            self.pos = 0
        logging.info("Visiting... Station is {} {}".format(self.stations[self.pos], self.name))
  
class AmState(State):
    """Separate Class for AM state of the radio"""  
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
  
    def toggle_amfm(self):
        """method for toggling the state"""
        logging.info("Switching to FM")
        self.radio.state = self.radio.fmstate
  
class FmState(State):
    """Separate class for FM state"""  
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
  
    def toggle_amfm(self):
        """method for toggling the state"""
        logging.info("Switching to AM")
        self.radio.state = self.radio.amstate
  
class Radio:
    """Dedicated class Radio"""
    """A radio. It has a scan button, and an AM / FM toggle switch."""
  
    def __init__(self):
        """We have an AM state and an FM state"""
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate
  
    def toggle_amfm(self):
        """Method to toggle the switch"""
        self.state.toggle_amfm()
  
    def scan(self):
        """Method to scan """
        self.state.scan()

def main():

    # Create radio object
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2
  
    for action in actions:
        action()

if __name__ == "__main__":
  main()
