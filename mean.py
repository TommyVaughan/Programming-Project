# Tommy Vaughan, 11/04/2018
# Calculating the mean of each column of the iris data set

import numpy
data = numpy.genfromtxt('Data/iris.csv', delimiter=',')
firstcol = data[:,0]