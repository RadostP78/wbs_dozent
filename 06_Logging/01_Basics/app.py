import logging

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


logging.basicConfig(filename="app.log", level = logging.DEBUG,
                    format = '%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s'  )


def add(x, y):
    result = x + y 

    logging.debug(f"X:{x}, y:{y} -> result:{result}")
    
    
    return result 
 
print(add(40,50))


logging.debug("This is a message")
logging.info("This is a message")
logging.warning("This is a message")
logging.error("This is a message")
logging.critical("This is a message")
logging.exception("This is a message")