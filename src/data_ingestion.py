import pandas as pd
import numpy as np
from logger_utils import setup_logger
import os

logger = setup_logger("logs/data_ingestions.log")
logger.info("Logging Set up for Data Ingestions Successfully!")

def load_data(file_path):

    """ Load the Datasets from the CSV File """

    try:
        if not os.path.exists(file_path):
            logger.error(f"File not Found:{file_path}")
            return None
        df = pd.read_csv(file_path)
        logger.info(f"Data Loaded Successfully from {file_path}")
        return df
        
    
    except Exception as e:
        logger.error(f"Error loading Data from {file_path}: {e}")
        return None

def save_data(df, output_path):

    """ Saves the Datasets to the output path"""

    try:

        os.makedirs(os.path.dirname(output_path), exist_ok= True)
        df.to_csv(output_path, index=False)
        logger.info(f"Data Saved Successfully to {output_path} ")

    except Exception as e:
        logger.error(f"Error saving data to {output_path}:{e}")

if __name__ == "__main__":
    
    df = load_data(r'data\kaggle\flight_price.csv')

    if df is not None:

        save_data(df,r'data\raw_data\flight_price.csv')
    
    print(df.head())




