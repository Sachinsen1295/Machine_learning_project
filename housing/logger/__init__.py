import logging
from datetime import datetime #to import current date time
import os

LOG_DIR= "housing_logs"

CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"log{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)  #to create directory we use makedirs

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename= LOG_FILE_PATH,
                    filemode = "w",
                    format = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
                    level = logging.INFO)