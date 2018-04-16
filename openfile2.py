with open("Data/iris.csv") as o:
 for line in o: 
  print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])) 
