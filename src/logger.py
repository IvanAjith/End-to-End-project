
## Step1: Basic Imports
import logging
import os
from datetime import datetime



## Step2 : Create a LOG FILE 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #Use this format to fetch LOG FILE
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)             #Create a path for that logfile 
os.makedirs(logs_path,exist_ok=True)                            #Create a Folder for Logging
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

##STEP 3: Create a Basic configuration for Logging 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)


