# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:31:38 2023

@author: mpatel
"""

import numpy as np
import matplotlib.pyplot as plt

# File path and name
file_path1 = r'C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Uniform thickness FEA results\load vs displacement 16_7g_2.csv'
file_path2 = r'C:\Users\mpatel\OneDrive - Niagara Bottling, LLC\Desktop\Niagara work backup\Shepley 750ml\Uniform thickness FEA results\load vs displacement 15g_2.csv'
# Load the CSV file
data1 = np.loadtxt(file_path1, delimiter=',')
data2 = np.loadtxt(file_path2, delimiter=',')
# Extract the data for x and y coordinates
x1 = data1[:, 0]
y1 = data1[:, 1]
x2 = data2[:, 0]
y2 = data2[:, 1]

# Plot the graph
plt.plot(x1, y1, label = '16.7g preform')
plt.plot(x2, y2, label = '15g preform')

# Customize the graph
plt.title('Top load comparison (FEA)')
plt.xlabel('Displacement')
plt.ylabel('Load (N)')
plt.legend(loc="upper right")
# Show the graph
plt.show()
