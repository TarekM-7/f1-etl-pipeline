import pandas as pd

def transform(results_df, drivers_df, races_df):
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
    return new_df

if __name__ == '__main__':
    from extract import extract_results, extract_drivers, extract_races

    results_df = extract_results('data/raw/results.csv')
    drivers_df = extract_drivers('data/raw/drivers.csv')
    races_df = extract_races('data/raw/races.csv')

    df = transform(results_df, drivers_df, races_df)
    print(df.head(20))
    print(df.shape)
