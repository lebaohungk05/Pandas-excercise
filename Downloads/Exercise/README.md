# Pandas Data Science Exercises

This project contains a series of exercises designed to build and reinforce data manipulation and analysis skills using the Python `pandas` library. Each exercise focuses on specific pandas functionalities, ranging from basic data creation to advanced grouping, merging, and visualization.

## Project Structure

The exercises are organized into folders by topic:

- **00_Creating_Series_and_DataFrames**: Basics of data structure creation (e.g., Pokemon data).
- **01_Getting_&_Knowing_Your_Data**: Loading and exploring datasets (e.g., Chipotle, Occupation, World Food Facts).
- **02_Filtering_&_Sorting**: Subsetting and ordering data (e.g., Euro 2012 stats).
- **03_Stats**: Working with statistical data and time series (e.g., US Baby Names, Wind Statistics).
- **04_Grouping**: Aggregating data based on categories (e.g., Alcohol Consumption, Regiment).
- **05_Apply**: Using the `apply` function for custom data transformations (e.g., Student Alcohol Consumption, US Crime Rates).
- **06_Merge**: Combining multiple datasets (e.g., Fictitious Names).
- **07_Visualization**: Creating plots and charts using `matplotlib` and `seaborn` (e.g., Online Retail, Titanic).
- **08_Deleting**: Handling missing data and removing columns/rows (e.g., Iris, Wine).

Each subdirectory contains:
- `Exercises.ipynb`: The original Jupyter Notebook with the task descriptions.
- `solutions.py`: A Python script containing the completed solutions for all tasks in that exercise.
- Data files (e.g., `.csv`, `.tsv`): The raw data used for the analysis.

## Prerequisites

To run these solutions, you need Python installed along with the following libraries:

```bash
pip install pandas matplotlib seaborn
```

## How to Run the Solutions

You can run any solution script directly using Python. Navigate to the specific exercise directory in your terminal and execute the `solutions.py` file.

**Example: Running the Pokemon exercise**

```bash
cd Exercise/00_Creating_Series_and_DataFrames/Pokemon
python solutions.py
```

The scripts are designed to print the results of each step to the console, allowing you to follow the data transformation process.

## Key Knowledge Areas

By completing these exercises, you will gain proficiency in:

1.  **Data Loading**: Handling different file formats (CSV, TSV) and using parameters like `sep` and `index_col`.
2.  **Exploratory Data Analysis (EDA)**: Using `head()`, `info()`, `describe()`, and `shape` to understand dataset structure.
3.  **Data Selection**: Mastering `.loc`, `.iloc`, and boolean indexing to filter data.
4.  **Aggregation**: Using `.groupby()` with functions like `sum()`, `mean()`, and `count()`.
5.  **Data Cleaning**: Renaming columns, changing data types, and handling missing values.
6.  **Functional Programming**: Applying custom functions to Series or DataFrames using `.apply()`, `.map()`, and `.applymap()`.
7.  **Data Merging**: Combining DataFrames using `pd.concat()` and `pd.merge()` (inner, outer, left, right joins).
8.  **Time Series**: Converting strings to datetime objects and resampling data (e.g., in Wind Stats).
9.  **Visualization**: Creating histograms, scatter plots, and bar charts to derive insights from data.

## Note on US Crime Rates Exercise
In `Exercise/05_Apply/US_Crime_Rates/`, the data file is named `student_alcohol.csv` but it actually contains the US Crime dataset. The `solutions.py` script correctly references this file to perform the analysis.
