import logging

logger = logging.getLogger()

class Car:

    def __init__(self) -> None:
        logger.debug("[Logger] car instance is created")

        print("Hallo Car instance")


    def show_car(self):
        logger.debug("[Logger] show_car method is called")
        print("VW Show car ")