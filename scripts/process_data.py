# Import necessary libraries
import pandas as pd

# Step 1: Read the raw data
raw_data_path = "../data/raw/frailty_data.csv"  # Correct relative path
frailty_data = pd.read_csv(raw_data_path)

# Step 2: Data cleaning and processing
# Convert the 'Frailty' column to a categorical variable
frailty_data['Frailty'] = frailty_data['Frailty'].astype('category')

# Step 3: Save the processed data
processed_data_path = "../data/processed/processed_frailty_data.csv"
frailty_data.to_csv(processed_data_path, index=False)

print("Data processing complete. Processed data saved to:", processed_data_path)