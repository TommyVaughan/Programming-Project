# Thomas Vaughan 19/04/2018
# To further analyse the data, I need to break it into it's three individual species
# I figured this out from https://www.novixys.com/blog/pandas-tutorial-select-dataframe/             
 

import pandas as pd                                                               # Import pandas library to help present data in nice format

pd.set_option("display.max_rows", 160)                                            # Allow all rows to be displayed in the dataset.
headers = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']   # Adding headers to the data
data = pd.read_csv("Data/iris.csv", names = headers)                              # Data is from the iris.csv file and also shows headers that are not in the csv file.

data[:]     
print(data[:50].describe())       # Shows only the data from the Setosa species in rows 0 to 49
# print(data[50:100].describe())  # Shows only the data from the Versicolor species in rows 50 to 99
# print(data[:50].describe())     # Shows only the data from the Virginica species in rows 100 to 149
