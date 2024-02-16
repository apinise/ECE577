import pandas as pd
import numpy as np
import seaborn as sns
import scipy.io
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def model_train(data_frame):
    X = data_frame['Timestamp']
    Y = data_frame[['Latitude','Longitude']]
    print(X)
    print(Y)

def create_dataset():
    # Import Mat Data
    mat1 = scipy.io.loadmat('week1.mat')
    mat2 = scipy.io.loadmat('week2.mat')
    mat3 = scipy.io.loadmat('week3.mat')
    mat4 = scipy.io.loadmat('week4.mat')
    # Create Heading
    data1 = mat1['week1']
    data2 = mat2['week2']
    data3 = mat3['week3']
    data4 = mat4['week4']
    # Convert to DataFrame
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    df4 = pd.DataFrame(data4)
    # Concatenating the dataframes vertically
    merged_df = pd.concat([df1, df2, df3, df4])
    merged_df.rename(columns= {0:'Timestamp', 1:'Latitude', 2:'Longitude', 3:'Accuracy', 4:'Label'}, inplace=True)
    # Sorting by the leftmost column
    merged_df = merged_df.sort_values(by='Timestamp')
    # Return Dataset
    return(merged_df)

df = create_dataset()
print(df)
model_train(df)
