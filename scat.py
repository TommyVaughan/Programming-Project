# Thomas Vaughan 12/04/2018.
# Opening the Iris data set to see the data in the csv file.
# Figured out how to use scatter plots here https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import pandas as pd                                                               # Adding all relevant libraries 
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
import numpy as nm

headers = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']   # Adding headers to the data
data = pd.read_csv("Data/iris.csv", names = headers) 


scatter_matrix(data)
plt.show