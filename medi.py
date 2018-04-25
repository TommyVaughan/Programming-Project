# Thomas Vaughan 12/04/2018.
# Calculate the mdian of each column of the Iris data set in the below script.
# Column = data[:,0] gives the first column. Insert # and remove from other comment to check the value of each column.
 

import numpy                                                # Read data file into array

data = numpy.genfromtxt('Data/iris.csv', delimiter=',')     # Reads a csv in array in numpy

column = data[:,0]                                          # To select all of the values column 1
medicol = numpy.median(data[:,0])                           # To get the median value column 1

# column = data[:,1]                                        # To select all of the values column 2
# medicol = numpy.median(data[:,1])                         # To get the median value column 2

# column = data[:,2]                                        # To select all of the values column 3
# medicol = numpy.median(data[:,2])                         # To get the median value column 3

# column = data[:,3]                                        # To select all of the values column 4
# medicol = numpy.median(data[:,3])                         # To get the median value column 4

print(medicol)