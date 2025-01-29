# Movie Data Analysis

This project explores and visualizes key insights from a movie dataset, originally included in the Udemy course **Python A-Z™: Python For Data Science With Real Exercises!** by Kirill Eremenko. The dataset, named `P4-Section6-Homework-Dataset.csv`, was leveraged to create unique visualizations that were not part of the course material.

## Dataset Information

The dataset contains information about movies, including:
- **Budget (in millions)**
- **Gross revenue (in millions)**
- **Adjusted gross revenue (inflation-adjusted, in millions)**
- **IMDb and MovieLens ratings**
- **Profit percentages**
- **Genres and Studios**
- **Runtime (in minutes)**

This dataset spans movies released over multiple decades, ranging from 1939 to 2015.

---

## Objective

The objective of this project was to practice Python visualization techniques by analyzing movie data and deriving actionable insights.

---

## Visualizations and Key Insights

### 1. **Genre Distribution**
![Genre Distribution](./Genre%20Distribution.png)
- **Insight**: The most dominant genre in the dataset is **Action**, followed by **Animation** and **Comedy**. Some genres, like **Documentary** and **Musical**, have a smaller representation.

### 2. **Yearly Trends of Adjusted Gross**
![Yearly Trends of Adjusted Gross](./Yearly%20Trends%20of%20Adjusted%20Gross.png)
- **Insight**: Adjusted gross revenue shows significant variance over the years. Older movies generally had higher adjusted gross values, potentially due to inflation adjustments.

### 3. **Correlation Heatmap of Numeric Columns**
![Correlation Heatmap of Numeric Columns](./Correlation%20Heatmap%20of%20Numeric%20Columns.png)
- **Insight**: 
  - `Adjusted Gross` and `Gross Revenue` have a strong positive correlation.
  - `Budget` shows a moderate correlation with `Gross Revenue`.
  - Ratings (`IMDb` and `MovieLens`) have a weak correlation with revenue-related columns.

### 4. **Top 10 Studios by Number of Movies**
![Top 10 Studios by Number of Movies](./Top%2010%20Studios%20by%20Number%20of%20Movies%20.png)
- **Insight**: Studios like **Buena Vista Studios**, **WB**, and **Fox** dominate the dataset in terms of the number of movies produced.

### 5. **Number of Movies Released Per Year**
![Number of Movies Released Per Year](./Number%20of%20Movies%20Released%20Per%20Year.png)
- **Insight**: There is a significant increase in the number of movies produced after 1980, peaking around 2010.

### 6. **Distribution of IMDb Ratings**
![Distribution of IMDb Ratings](./Distribution%20of%20IMDb%20Ratings.png)
- **Insight**: The ratings are approximately normally distributed, with the mean and median both around **6.9**.

### 7. **Distribution of Gross Millions by Genre**
![Distribution of Gross Millions by Genre](./Distribution%20of%20Gross%20Millions%20by%20Genre.png)
- **Insight**: Genres like **Sci-Fi**, **Adventure**, and **Animation** show higher gross values on average. The data has significant outliers.

### 8. **Relationship between Budget and Gross Revenue**
![Relationship between Budget and Gross Revenue](./Relationship%20between%20budget%20and%20gross%20revenue.png)
- **Insight**: A positive trend is observed between **Budget** and **Gross Revenue**, indicating higher-budget movies tend to gross more.

---

## Tools Used

- **Python Libraries**:
  - `pandas` for data manipulation
  - `matplotlib` and `seaborn` for data visualization
  - `numpy` for numeric operations

---

## How to Reproduce

1. Clone this repository:
```bash
https://github.com/<your-username>/<repository-name>.git
```

2. Install required libraries:
```bash
pip install pandas matplotlib seaborn numpy
```

3. Run the provided Python script or Jupyter Notebook.

---

## Acknowledgments

The dataset is sourced from the **Udemy course** "Python A-Z™: Python For Data Science With Real Exercises!" by **Kirill Eremenko**. The visualizations and insights derived in this project are independently created as part of a learning exercise.

---

## License

This project is for educational purposes only and follows the licensing terms of the Udemy course dataset. Redistribution of the dataset without explicit permission is not allowed.
