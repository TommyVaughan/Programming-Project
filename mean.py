# Thomas Vaughan 12/04/2018
# Calculate the mean of each column of the iris data set
# In the below script, to check the mean of each colum: 
# For column = data[:,0] gives the first column
# Change both the 0's to 1's to get the second column, 2 for the third and so on 


import numpy
# Read data file into array
data = numpy.genfromtxt('Data/iris.csv', delimiter=',')

column = data[:,3]    
meancol = numpy.mean(data[:,3])
print(meancol)












# mean of col 1 = 5.843
# mean of col 2 = 3.054
# mean of col 3 = 3.758
# mean of col 4 = 1.20