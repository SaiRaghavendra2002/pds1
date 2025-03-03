# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the processed data
processed_data_path = "../data/processed/processed_frailty_data.csv"
frailty_data = pd.read_csv(processed_data_path)

# Step 2: Create visualizations

# Visualization 1: Scatter plot of Grip Strength vs. Age
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Grip Strength', hue='Frailty', data=frailty_data)
plt.title("Grip Strength vs. Age")
plt.xlabel("Age")
plt.ylabel("Grip Strength (kg)")
plt.savefig("../output/figures/grip_strength_vs_age.png")
plt.show()

# Visualization 2: Box plot of Grip Strength by Frailty
plt.figure(figsize=(8, 6))
sns.boxplot(x='Frailty', y='Grip Strength', data=frailty_data)
plt.title("Grip Strength by Frailty")
plt.xlabel("Frailty")
plt.ylabel("Grip Strength (kg)")
plt.savefig("../output/figures/grip_strength_by_frailty_boxplot.png")
plt.show()