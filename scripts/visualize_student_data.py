# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create the output directory if it doesn't exist
output_dir = "../output/figures/student_performance"
os.makedirs(output_dir, exist_ok=True)

# Step 1: Read the student performance dataset
student_data_path = "../data/raw/student_performance.csv"
student_data = pd.read_csv(student_data_path)

# Print column names to verify
print(student_data.columns)

# Step 2: Perform 5 data visualization tasks

# Visualization 1: Histogram of Math Scores
plt.figure(figsize=(8, 6))
sns.histplot(student_data['math score'], bins=10, kde=True, color='blue')
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.savefig(os.path.join(output_dir, "math_score_histogram.png"))
plt.show()

# Visualization 2: Scatter Plot of Math vs. Reading Scores
plt.figure(figsize=(8, 6))
sns.scatterplot(x='math score', y='reading score', data=student_data, color='green')
plt.title("Math vs. Reading Scores")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.savefig(os.path.join(output_dir, "math_vs_reading_scatter.png"))
plt.show()

# Visualization 3: Box Plot of Writing Scores by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='writing score', data=student_data, palette='pastel')
plt.title("Writing Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Writing Score")
plt.savefig(os.path.join(output_dir, "writing_score_by_gender_boxplot.png"))
plt.show()

# Visualization 4: Bar Plot of Average Scores by Ethnicity
avg_scores = student_data.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean()
avg_scores.plot(kind='bar', figsize=(10, 6))
plt.title("Average Scores by Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Average Score")
plt.savefig(os.path.join(output_dir, "average_scores_by_ethnicity_barplot.png"))
plt.show()

# Visualization 5: Heatmap of Correlation Between Scores
corr_matrix = student_data[['math score', 'reading score', 'writing score']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Between Scores")
plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
plt.show()