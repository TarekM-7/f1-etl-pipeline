from etl.extract import extract_results, extract_drivers, extract_races
from etl.transform import transform
from etl.load import load

if __name__ == '__main__':

    results_df = extract_results('data/raw/results.csv')
    drivers_df = extract_drivers('data/raw/drivers.csv')
    races_df = extract_races('data/raw/races.csv')

    df = transform(results_df, drivers_df, races_df)
    
    load(df, 'data/processed/f1_driver_career_stats.csv', 'processed/f1_driver_career_stats.csv')
    