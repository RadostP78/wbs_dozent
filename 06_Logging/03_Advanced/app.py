import logging
from logging.config import fileConfig

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)




# Configure the logger from external file
fileConfig("./logging.ini", disable_existing_loggers = False)


logger = logging.getLogger()

logger.debug("Hallo Advanced Logger 2")

