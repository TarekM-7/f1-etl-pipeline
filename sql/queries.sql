SELECT 
    year, avg_position, races_entered 
FROM 
    'data/processed/f1_driver_career_stats.csv' 
WHERE 
    forename = 'Max' 
    and 
    surname = 'Verstappen'