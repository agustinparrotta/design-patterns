import logging
import time

logging.basicConfig(level='INFO')

class Producer:
    """Define the 'resource-intensive' object to instantiate."""
    def produce(self) -> None:
        logging.info('Producer is working hard!')

    def meet(self) -> None:
        logging.info('Producer has time to meet you now!')


class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman."""
    def __init__(self) -> None:
        self.occupied = False
        self.producer = None

    def produce(self) -> None:
        """ Check if Producer is available """
        logging.info('Artist checking if Product is available...')

        if not self.occupied:
            # If the producer is available, create a producer object!
            producer = Producer()

            # Make the producer meet the guest!
            producer.meet()
        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            logging.info('Producer is busy!')


def main() -> None:
    # Instantiate a Proxy
    proxy = Proxy()

    # Make the proxy: Artist produce until Producer is available
    proxy.produce()

    # Change the sate to 'ocuppied'
    proxy.occupied = True

    # Make the Producer produce
    proxy.produce()


if __name__ == '__main__':
    main()