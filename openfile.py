# Thomas Vaughan 12/04/2018.
# Opening the Iris data set to see the data in the csv file.

import pandas as pd                                                               # Import pandas library to help present data in nice format

pd.set_option("display.max_rows", 160)                                            # Allow all rows to be displayed in the dataset.
headers = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']   # Adding headers to the data
data = pd.read_csv("Data/iris.csv", names = headers)                              # Data is from the iris.csv file and also shows headers that are not in the csv file.

data[:]                                                                           # Show all the data in the file 
print(data)                                                              


# print(data.shape) to view the total number of rows and columns in the dataset.
# print(data.groupby('Species').size()) to break the data into the three species.