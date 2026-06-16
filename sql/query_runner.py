import duckdb

conn = duckdb.connect()

with open("sql/queries.sql", "r") as file:
    query = file.read()
    
df = conn.execute(query).df()

print(df)