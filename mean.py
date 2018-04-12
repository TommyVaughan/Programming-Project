# Thomas Vaughan 12/04/2018
# Calculate the mean of each column of the iris data set
# In the below script, to check the mean of each colum: 
# For column = data[:,0] gives the first column
# Change both the 0's to 1's to get the second column, 2 for the third and so on 


import numpy
# Read data file into array
data = numpy.genfromtxt('Data/iris.csv', delimiter=',')
# To select all of the values of a column
column = data[:,0]    
# To get the mean value of that column
meancol = numpy.mean(data[:,0])
print(meancol)





# mean of col 1 = 5.843
# mean of col 2 = 3.054
# mean of col 3 = 3.758
# mean of col 4 = 1.198