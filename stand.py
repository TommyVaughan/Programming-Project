# Thomas Vaughan 12/04/2018.
# Calculate the standard deviation of each column of the Iris data set in the below script.
# Column = data[:,0] gives the first column.
# To calculate each column, change both the 0's to 1's to get the second column, 2 for the third and so on.


import numpy                                              # Read data file into array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')   # Reads a csv in array in numpy

column = data[:,0]                                        # To select all of the values of a column

stand = numpy.std(data[:,0])                              # To get the standard deviation value of that column
print(stand)




# standard deviation of col 1 (Sepal-length)  = 0.825
# standard deviation of col 2 (Sepal-width)   = 0.432
# standard deviation of col 3 (Petal-lenght)  = 1.758
# standard deviation of col 4 (Petal-width)   = 0.760