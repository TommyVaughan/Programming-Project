# Thomas Vaughan 12/04/2018.
# Calculate the mean of each column of the Iris data set in the below script.
# Column = data[:,0] gives the first column. Insert # and remove from other comment to check the value of each column.

import numpy                                                # Read data file into array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')     # Reads a csv in array in numpy

column = data[:,0]                                          # To select all of the values column 1
meancol = numpy.mean(data[:,0])                             # To get the mean value column 1

# column = data[:,1]                                        # To select all of the values column 2
# meancol = numpy.mean(data[:,1])                           # To get the mean value column 2

# column = data[:,2]                                        # To select all of the values column 3
# meancol = numpy.mean(data[:,2])                           # To get the mean value column 3

# column = data[:,3]                                        # To select all of the values column 4
# meancol = numpy.mean(data[:,3])                           # To get the mean value column 4

print(meancol)





# import matplotlib.pyplot as mp                            # import the matplotlib pyplot library
# mp.hist(column)                                           # generate a histogram
# mp.show()                                                 # show the histogram