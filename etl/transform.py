import pandas as pd
import logging

logging.basicConfig(
    format='[{levelname}] {asctime} | {message}',
    style='{',
    datefmt='%H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def transform(results_df, drivers_df, races_df):
    try:
        logger.info("Starting data transformation stage")
        joined_df = (
            results_df
            .merge(drivers_df, how='left', on='driverId')
            .merge(races_df, how='left', on='raceId')
        )
        new_df = (
            joined_df
            .groupby(['driverId', 'year'], as_index=False)
            .agg(
                forename=('forename', 'first'),
                surname=('surname', 'first'),
                avg_position = ('positionOrder', 'mean'),
                races_entered=('resultId', 'count')
            )
            .round({'avg_position': 2})
        )
        logger.info(f"Transformation complete: {len(new_df)} driver-season records produced")
        return new_df
    except Exception as e:
        logger.error(f"Error transforming the data: {e}")
        raise      

# if __name__ == '__main__':
#     from extract import extract_results, extract_drivers, extract_races

#     results_df = extract_results('data/raw/results.csv')
#     drivers_df = extract_drivers('data/raw/drivers.csv')
#     races_df = extract_races('data/raw/races.csv')

#     df = transform(results_df, drivers_df, races_df)
#     print(df.head(20))
#     print(df.shape)
#     print(df['avg_position'].isnull().sum())
#     print(df[(df['forename'] == 'Lewis') & (df['year'] == 2008)])
#     print(df[(df['forename'] == 'Max') & (df['year'] == 2023)])
