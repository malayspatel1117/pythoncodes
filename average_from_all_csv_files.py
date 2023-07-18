# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:57:29 2023

@author: mpatel
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_csv_files(file_paths):
    dataframes = [pd.read_csv(file) for file in file_paths]
    return dataframes

def calculate_average(dataframes):
    average_data = pd.concat(dataframes).groupby(level=0).mean()
    return average_data

def plot_xy_graph(average_data):
    x_values = average_data.index
    y_values = average_data.values.T  # Transpose to get individual columns as y values
    for i, y in enumerate(y_values):
        plt.plot(x_values, y, label=f'Column {i+1}')
    plt.xlabel('X Values')
    plt.ylabel('Average Y Values')
    plt.legend()
    plt.title('XY Graph of Averages')
    plt.show()

if __name__ == "__main__":
    file_paths = [
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book2.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book3.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book5.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book6.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book7.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book8.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book9.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book10.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book11.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book12.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book13.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book14.csv",
        r"C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Book15.csv"
        # Add more file paths as needed
    ]
    
    dataframes = load_csv_files(file_paths)
    if len(dataframes) == 0:
        print("No CSV files found at the specified file paths.")
    else:
        average_data = calculate_average(dataframes)
        plot_xy_graph(average_data)
