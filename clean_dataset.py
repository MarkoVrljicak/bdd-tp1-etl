import pandas as pd

# Load the CSV file
file_path = 'olympic_medals_2022_dirty.csv'
df = pd.read_csv(file_path, thousands=',')

# Remove the first autoincremental column
df = df.drop(df.columns[0], axis=1)
df = df.drop('SOG_total_medals', axis=1)
df = df.drop('WOG_total_medals', axis=1)

# Split the 'team' column into 'country_name' and 'country_code', ignoring values in square brackets
df[['country_name', 'country_code']] = df['team'].str.extract(r'([^\[]+)\s+\(([A-Z0-9]+)\)', expand=True)

# Drop the original 'team' column
df = df.drop('team', axis=1)

# Reorder columns to place 'country_name' and 'country_code' at the beginning
cols = ['country_name', 'country_code'] + [col for col in df.columns if col not in ['country_name', 'country_code']]
df = df[cols]

# Save the modified DataFrame to a new CSV file
output_path = 'olympic_medals_2022_clean.csv'
df.to_csv(output_path, index=False)