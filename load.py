import pandas as pd
import sqlite3

# Load the CSV file
file_path = 'olympic_medals_2022_clean.csv'
df = pd.read_csv(file_path)

# Rename the columns to make them more readable
df.columns = [
    'country_name',
    'country_code',
    'summer_olympics_participated',
    'summer_olympics_gold',
    'summer_olympics_silver',
    'summer_olympics_bronze',
    'winter_olympics_participated',
    'winter_olympics_gold',
    'winter_olympics_silver',
    'winter_olympics_bronze'
]

# Create a SQLite database and establish a connection
db_path = 'olympic_medals_2022.db'
conn = sqlite3.connect(db_path)

# Dump the DataFrame into an SQLite table
df.to_sql('olympic_medals', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data has been successfully dumped into the SQLite database.")
