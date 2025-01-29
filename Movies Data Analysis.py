import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# os.getcwd()

"""1) Import Data"""
movie_data = pd.read_csv('C:\\Users\\MichaelP\\Desktop\\Udemy Courses and files\\Python\\Udemy Python\\'
                     'Python A-Z Python For Data Science With Real Exercises\\Section 6\\'
                        'P4-Section6-Homework-Dataset.csv', encoding = 'latin1')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

"""2) Renaming Columns"""
movie_data.columns = ['day_of_week', 'director', 'genre', 'movie_title', 'release_date', 'studio', 'adjusted_gross_millions',
                      'budget_millions', 'gross_millions', 'imdb_rating', 'movie_lens_rating',
                      'overseas_millions', 'overseas_%', 'profit_millions', 'profit_%', 'runtime_minutes', 'us_millions',
                      'Gross%US']

"""3) Check general info"""
# print(len(movie_data))
# print(movie_data.head(10))
# print(movie_data.columns)
# movie_data.info()
# print(movie_data.describe())
# print(len(movie_data.columns))

"""4) Check for Missing Values"""
# print(movie_data.isnull().sum())

"""5) Data Types"""
# Extract the year from release_year column for time-based analysis
movie_data['release_year'] = pd.to_datetime(movie_data['release_date'], errors='coerce').dt.year

# Set Data Types for efficiency
# print(len(movie_data.release_year.unique()))
movie_data['day_of_week'] = movie_data['day_of_week'].astype('category')
movie_data['release_year'] = movie_data['release_year'].astype('category')
movie_data['genre'] = movie_data['genre'].astype('category')
movie_data['studio'] = movie_data['studio'].astype('category')
movie_data['gross_millions'] = pd.to_numeric(movie_data['gross_millions'], errors='coerce')
# print(movie_data.dtypes)

"""6) Check for Duplicates"""
# print(f"Number of duplicate rows: {movie_data.duplicated().sum()}")
duplicates = movie_data[movie_data.duplicated()]
movie_data.drop_duplicates(inplace=True)
# print(f"Number of duplicate rows after dropping: {movie_data.duplicated().sum()}")

"""7) Visualizations"""

"""Bar Chart: Top 10 Studios by Number of Movies"""
# # Count movies by studio and get the top 10
# studio_counts = movie_data['studio'].value_counts().head(10).reset_index()
# studio_counts.columns = ['studio', 'movie_count']
# # Sort by movie count for better visual order
# studio_counts = studio_counts.sort_values(by='movie_count', ascending=False)
#
# # print(studio_counts)
# plt.close('all')
# plt.clf()
# sns.reset_defaults()
# plt.figure(figsize = (12, 8))
# sns.barplot(data=studio_counts, x='studio', y='movie_count', palette = 'coolwarm')
# plt.title('Top 10 Studios by Movies', fontsize=16, fontweight='bold')
# plt.xlabel('Studio',  fontsize=12)
# plt.ylabel('Number of Movies', fontsize=12)
# plt.xticks(rotation=45, ha='right') # Rotate labels and align them to the right
# plt.tight_layout()
# plt.show()

# Top 10 Studios Data (Manually Verified)
studio_counts = pd.DataFrame({
    'studio': [
        'Buena Vista Studios', 'WB', 'Fox', 'Universal', 'Sony',
        'Paramount Pictures', 'Pacific Data/DreamWorks', 'New Line Cinema',
        'DreamWorks', 'TriStar'
    ],
    'movie_count': [93, 93, 85, 79, 65, 62, 16, 16, 14, 10]
})

# Convert to DataFrame
studio_counts_df = pd.DataFrame(studio_counts)
# Clear any previous plots
plt.close('all')  # Close any lingering figures
plt.clf()  # Clear the current figure
sns.reset_defaults()  # Reset Seaborn styles
# Plot the Top 10 Studios
plt.figure(figsize=(12, 8))
sns.barplot(data=studio_counts_df, x='studio', y='movie_count', palette='coolwarm')
# Add legend manually
handles = [plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=color, markersize=10, label=studio)
    for studio, color in zip(studio_counts_df['studio'], sns.color_palette('coolwarm', len(studio_counts_df)))]
plt.legend(handles=handles, title='Studios', bbox_to_anchor=(1.05, 1), loc='upper left')
# Customize the Plot
plt.title('Top 10 Studios by Number of Movies', fontsize=16, fontweight='bold')
plt.xlabel('Studio', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.ylim(0, 100)  # Set y-axis range from 0 to 100
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


"""Number of Movies Released Per Year"""
# print(sorted(movie_data.release_year.unique()))
movie_count_per_year = movie_data.release_year.value_counts().sort_index()
# print(movie_count_per_year)
plt.figure(figsize=(12, 8))
plt.plot(movie_count_per_year.index, movie_count_per_year.values, marker='o')
plt.title('Number of Movies Released Per Year', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.xlim(1930, 2020)
plt.ylabel('Number of Movies', fontsize=12)
plt.grid(True)


"""Distribution of IMDb Ratings"""
plt.figure(figsize=(10, 6))
sns.histplot(data=movie_data, x='imdb_rating', bins=20, kde=True, color='blue')
plt.title('Distribution of IMDb Ratings', fontsize=16, fontweight='bold')
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.7)
mean_rating = movie_data['imdb_rating'].mean()
median_rating = movie_data['imdb_rating'].median()
plt.axvline(mean_rating, color='red', linestyle='--', label=f'Mean: {mean_rating:.2f}')
plt.axvline(median_rating, color='green', linestyle='--', label=f'Median: {median_rating:.2f}')
plt.legend()


"""Genre vs. Gross Millions"""
# print(sorted(movie_data.genre.unique()))
# print(len(movie_data.genre.unique()))
# Filter out very small gross values
# movie_data_filtered = movie_data[movie_data['gross_millions'] > 1]
# Order genres by median gross
order = movie_data.groupby('genre')['gross_millions'].median().sort_values(ascending=False).index
plt.figure(figsize=(12, 8))
sns.boxplot(data=movie_data, x='gross_millions', y='genre', order=order, palette='Set2')
sns.stripplot(data=movie_data, x='gross_millions', y='genre', color='black', alpha=0.5, size=2, jitter=True)
plt.xscale('log')
plt.title('Distribution of Gross Millions by Genre', fontsize=16, fontweight='bold')
plt.xlabel('Gross Millions (Log scale)', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()


"""Budget vs. Gross"""
plt.figure(figsize=(12, 8))
plt.scatter(data=movie_data, x='budget_millions', y='gross_millions', marker='o', alpha=0.5)
sns.regplot(data=movie_data, x='budget_millions', y='gross_millions', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relationship between budget and gross revenue', fontsize=16, fontweight='bold')
plt.ylabel('Gross Revenue (in Millions of Dollars)', fontsize=12)
plt.xlabel('Budget (in Millions of Dollars)', fontsize=12)
plt.xlim(0, 300)
plt.ylim(0, 1000)
plt.grid(True, linestyle='--', alpha=0.7)



"""Genre Distribution"""
# Step 1: Count the number of movies in each genre
genre_counts = movie_data['genre'].value_counts()
# print(genre_counts)
# Step 2: Extract data for the pie chart
labels = genre_counts.index # Genres
sizes = genre_counts.values # Number of movies in each genre
explode = [0.1 if size < 5 else 0 for size in sizes]  # Explode slices smaller than 5%
plt.figure(figsize=(15, 12))
def autopct_format(pct):
    return f'{pct:.1f}%' if pct > 2 else ''  # Only show percentages > 2%
plt.pie(sizes, labels=None, autopct=autopct_format, startangle=90, wedgeprops={'edgecolor': 'black'}, colors=plt.cm.Set3.colors)
plt.legend(labels, title='Genres', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=14, title_fontsize=16)
plt.title('Genre Distribution', fontsize=16, fontweight='bold')
plt.tight_layout()


"""Yearly Trends of Adjusted Gross"""
movie_data['adjusted_gross_millions'] = pd.to_numeric(movie_data['adjusted_gross_millions'], errors='coerce') # Ensure adjusted_gross_millions is numeric
yearly_data = movie_data.groupby('release_year')['adjusted_gross_millions'].mean().reset_index() # Group data by year and calculate the mean adjusted gross
# Extract years and adjusted gross for plotting
years = yearly_data['release_year']
adjusted_gross = yearly_data['adjusted_gross_millions']

plt.figure(figsize=(12, 8))
plt.plot(years, adjusted_gross, linestyle='--', color='blue', marker='o')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.0f}'))  # Format as whole numbers
plt.gca().yaxis.set_major_locator(ticker.LogLocator(base=10.0, subs=np.arange(1, 10) * 0.1, numticks=10))
plt.title('Yearly Trends of Adjusted Gross', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adjusted Gross (in Millions of Dollars)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()


"""Correlation Between Numeric Columns"""
# Step 1: Select numeric columns
numeric_cols = movie_data.select_dtypes(include=['float64', 'int64'])
# Step 2: Compute the correlation matrix
correlation_matrix = numeric_cols.corr()
# Step 3: Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, square=True)
plt.title('Correlation Heatmap of Numeric Columns', fontsize=16, fontweight='bold')
plt.tight_layout()

plt.show()


