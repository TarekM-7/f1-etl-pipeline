import pandas as pd

def extract_results(path):
    raw_df = pd.read_csv(path, na_values='\\N')
    columns = ['resultId', 'raceId', 'driverId', 'positionOrder', 'statusId']
    new_df = raw_df[columns]
    return new_df

def extract_drivers(path):
    raw_df = pd.read_csv(path, na_values='\\N')
    columns = ['driverId', 'forename', 'surname']
    new_df = raw_df[columns]
    return new_df

def extract_races(path):
    raw_df = pd.read_csv(path, na_values='\\N')
    columns = ['raceId', 'year', 'name']
    new_df = raw_df[columns]
    return new_df