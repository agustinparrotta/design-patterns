import logging
from typing import List

logging.basicConfig(level='INFO')


class Handler:
    """Abstract Handler."""
    def __init__(self, successor: object) -> None:
        # Define who is the next handler
        self._successor = successor

    def handle(self, request: int) -> None:
        handled = self._handle(request) # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)


class ConcreteHandler1(Handler): # Inherits from the abstract handler
    """Concrete handler 1."""
    def _handle(self, request: int) -> bool:
        if 0 < request <= 10:   # Provide a condition for handling
            logging.info('Request {} handled in the handler 1'.format(request))
            return True # Indicates that the request has been handled


class DefaultHandler(Handler):  # Inherits from the abstract handler
    """Default handler."""
    def _handle(self, request: int) -> bool:
        """ If there is no handler available """
        # No condition checking since this is a default handler
        logging.info('End of chain, no handler for {}'.format(request))
        return True # Indicates that the request has been handled


class Client:   # Using handlers
    
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))   # Create handlers and use them in a sequence you want
                                                                # Note that the default handler has no successor

    def delegate(self, requests: List[int]) -> None: # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


def main() -> None:
    # Create a client
    client = Client()

    # Create requests
    requests = [2, 5, 30]

    # Send the requests
    client.delegate(requests)


if __name__ == '__main__':
    main()