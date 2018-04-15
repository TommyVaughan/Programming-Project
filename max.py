# Thomas Vaughan 12/04/2018.
# Calculate the maximum of each column of the Iris data set in the below script.
# Column = data[:,0] gives the first column.
# To calculate each column, change both the 0's to 1's to get the second column, 2 for the third and so on.


import numpy                                              # Read data file into array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')   # Reads a csv in array in numpy

column = data[:,0]                                        # To select all of the values of a column

maxcol = numpy.max(data[:,0])                             # To get the maximum value of that column
print(maxcol)




# max of col 1 (Sepal-length)  = 7.9
# max of col 2 (Sepal-width)   = 4.4
# max of col 3 (Petal-lenght)  = 6.9
# max of col 4 (Petal-width)   = 2.5