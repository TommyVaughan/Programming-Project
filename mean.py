# Thomas Vaughan 12/04/2018.
# Calculate the mean of each column of the Iris data set in the below script.
# Column = data[:,0] gives the first column.
# To calculate each column, change both the 0's to 1's to get the second column, 2 for the third and so on.

import numpy                                              # Read data file into array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')   # Reads a csv in array in numpy

column = data[:,0]                                        # To select all of the values of a column

meancol = numpy.mean(data[:,0])                           # To get the mean value of that column
print(meancol)


# mean of col 1 (Sepal-length)  = 5.843
# mean of col 2 (Sepal-width)   = 3.054
# mean of col 3 (Petal-lenght)  = 3.758
# mean of col 4 (Petal-width)   = 1.198

import matplotlib.pyplot as mp      # import the matplotlib pyplot library
mp.hist(column)                     # generate a histogram
mp.show()                           # show the histogram