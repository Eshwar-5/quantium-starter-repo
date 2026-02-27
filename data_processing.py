import pandas as pd
import os

# Define the path to your data folder
data_folder = './data'
output_file = 'formatted_output.csv'

# List to hold dataframes
dfs = []

# Loop through the files you found
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)

        # 1. Filter for Pink Morsels only
        df = df[df['product'] == 'pink morsel']

        # 2. Fix the price (remove '$') and calculate sales
        df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
        df['sales'] = df['price'] * df['quantity']

        # 3. Keep only the required columns
        df = df[['sales', 'date', 'region']]
        dfs.append(df)

# Combine all processed data into one file
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv(output_file, index=False)

print(f"Success! {output_file} has been created.")