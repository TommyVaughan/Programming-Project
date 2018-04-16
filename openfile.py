# Thomas Vaughan 12/04/2018.
# Opening the Iris data set in VS to see the data


with open("Data/iris.csv") as o:
  print(o.read())  # Reads the file into memory and prints the file

