import logging

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)

from europcar.car import Car


# Create a logger 
logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')


# File Handler logger 
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

# Stream Handler: Terminal
stream_handler = logging.StreamHandler() 

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)



logger.debug("Hallo Mohamed")


car1 = Car() 

car1.show_car()