

import numpy                                              # Read data file into array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')   # Reads a csv in array in numpy

column = data[:,0]                                        # To select all of the values of a column

mincol = numpy.min(data[:,0])                           # To get the mean value of that column
print(mincol)

