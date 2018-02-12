import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = os.getcwd() + '/ex1/ex1data1.txt'
data = pd.read_csv(path, header = None, names = ['Population', 'Profit'])
print data.head()