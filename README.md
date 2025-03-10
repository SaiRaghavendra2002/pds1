

---

```markdown
# Assignment 1

This repository contains the code and data for **Assignment 1**, which involves data processing and visualization tasks on two datasets:
1. **Frailty Dataset**: Analyzing the relationship between grip strength, age, weight, and frailty in females.
2. **Student Performance Dataset**: Visualizing student performance in math, reading, and writing scores.

---

## **Folder Structure**

```
Assignment1/
├── data/
│   ├── raw/                  # Contains raw datasets
│   │   ├── frailty_data.csv            # Frailty dataset
│   │   └── student_performance.csv     # Student performance dataset
│   └── processed/            # Contains processed datasets
│       └── processed_frailty_data.csv  # Processed frailty dataset
├── scripts/                  # Contains Python scripts for data processing and visualization
│   ├── process_data.py       # Processes the frailty dataset
│   ├── visualize_data.py     # Visualizes the frailty dataset
│   └── visualize_student_data.py # Visualizes the student performance dataset
└── output/                   # Contains generated figures and reports
    └── figures/
        ├── grip_strength_vs_age.png              # Scatter plot: Grip Strength vs. Age
        ├── grip_strength_by_frailty_boxplot.png  # Box plot: Grip Strength by Frailty
        └── student_performance/                  # Visualizations for student performance dataset
            ├── math_score_histogram.png          # Histogram: Math Scores
            ├── math_vs_reading_scatter.png       # Scatter plot: Math vs. Reading Scores
            ├── writing_score_by_gender_boxplot.png # Box plot: Writing Scores by Gender
            ├── average_scores_by_ethnicity_barplot.png # Bar plot: Average Scores by Ethnicity
            └── correlation_heatmap.png           # Heatmap: Correlation Between Scores
```

---

## **How to Run**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Assignment1.git
   cd Assignment1
   ```

2. **Install Dependencies:**
   Ensure you have the required Python libraries installed:
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. **Run the Scripts:**
   - Process the frailty dataset:
     ```bash
     python scripts/process_data.py
     ```
   - Visualize the frailty dataset:
     ```bash
     python scripts/visualize_data.py
     ```
   - Visualize the student performance dataset:
     ```bash
     python scripts/visualize_student_data.py
     ```

4. **Check the Output:**
   - Processed data will be saved in `data/processed/`.
   - Visualizations will be saved in `output/figures/`.

---

## **Results**

### Frailty Dataset Visualizations
1. **Grip Strength vs. Age:**
   - A scatter plot showing the relationship between grip strength and age, colored by frailty status.
2. **Grip Strength by Frailty:**
   - A box plot comparing grip strength between frail and non-frail participants.

### Student Performance Dataset Visualizations
1. **Distribution of Math Scores:**
   - A histogram showing the distribution of math scores.
2. **Math vs. Reading Scores:**
   - A scatter plot showing the relationship between math and reading scores.
3. **Writing Scores by Gender:**
   - A box plot comparing writing scores between genders.
4. **Average Scores by Ethnicity:**
   - A bar plot showing average math, reading, and writing scores by ethnicity.
5. **Correlation Between Scores:**
   - A heatmap showing the correlation between math, reading, and writing scores.

---

## **Dependencies**
- Python 3.x
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

---

## **Author**
- **Sai Raghavendra Katragadda**
- **Contact:** skt54@umsystem.edu


---
