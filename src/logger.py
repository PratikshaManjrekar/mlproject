# For logging the execution in some files so that we will be able to tract exceptions,errors and to log that into particular fie
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"     # File name format
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   #Whatever logs get created it'll be respect to current working directeory
os.makedirs(logs_path,exist_ok=True)  # Even though there is a file it'll keep on appending

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")