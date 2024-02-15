import pandas as pd
import numpy as np
import seaborn as sns
import scipy.io
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Convert to DataFrame
mat = scipy.io.loadmat('week1.mat')

data = mat['week1']
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Assuming you have two dataframes df1 and df2
# with the same number of columns (5 columns) and sorted by the leftmost column

# Example dataframes
data1 = {
    'A': [1, 3, 5],
    'B': [2, 4, 6],
    'C': [8, 10, 12],
    'D': [9, 11, 13],
    'E': [14, 15, 16]
}

data2 = {
    'A': [2, 4, 6],
    'B': [3, 5, 7],
    'C': [9, 11, 13],
    'D': [10, 12, 14],
    'E': [17, 18, 19]
}

data3 = {
    'A': [3, 5, 7],
    'B': [4, 6, 8],
    'C': [10, 12, 14],
    'D': [11, 13, 15],
    'E': [20, 21, 22]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Concatenating the dataframes vertically
merged_df = pd.concat([df1, df2, df3])

# Sorting by the leftmost column
merged_df = merged_df.sort_values(by='A')

print(merged_df)

