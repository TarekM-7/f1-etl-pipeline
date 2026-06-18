import pandas as pd
import logging
from etl.logger import get_logger
logger = get_logger(__name__)

def extract_results(path):
    try:
        logger.info(f"Extracting results from {path}")
        raw_df = pd.read_csv(path, na_values='\\N')
        columns = ['resultId', 'raceId', 'driverId', 'positionOrder', 'statusId']
        new_df = raw_df[columns]
        logger.info(f"Results extracted: {len(new_df)} rows")
        return new_df
    except Exception as e:
        logger.error(f"Error extracting results data: {e}")
        raise
        
def extract_drivers(path):
    try:
        logger.info(f"Extracting drivers from {path}")
        raw_df = pd.read_csv(path, na_values='\\N')
        columns = ['driverId', 'forename', 'surname']
        new_df = raw_df[columns]
        logger.info(f"Drivers extracted: {len(new_df)} rows")
        return new_df
    except Exception as e:
        logger.error(f"Error extracting drivers data: {e}")
        raise
        
def extract_races(path):
    try:
        logger.info(f"Extracting races from {path}")
        raw_df = pd.read_csv(path, na_values='\\N')
        columns = ['raceId', 'year', 'name']
        new_df = raw_df[columns]
        logger.info(f"Races extracted: {len(new_df)} rows")
        return new_df
    except Exception as e:
        logger.error(f"Error extracting races data: {e}")
        raise