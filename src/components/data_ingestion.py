import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass     # For creating class variables

@dataclass        
# If you are defining only variables then use dataclass decorator 
# If you have other functions go with __init__ and don't use this decorator
class DataIngestionConfig:    
    train_data_path: str=os.path.join('artifacts',"train.csv") #input that we are giving
    # All the outputs will be stored in artifacts folder and file name will be train.csv
    test_data_path: str=os.path.join('artifacts',"test.csv")   #i/p
    raw_data_path: str=os.path.join('artifacts',"data.csv")    #i/p

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        # If data is stored in database, it will read from the database
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            # Here we can read the dataset from mongodb or mysql
            logging.info('Read the dataset as datafrmae')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()