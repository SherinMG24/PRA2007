import math

def openfile(filename):
    #creat a empty list to then add the data points from the file into it
    data = []
    with open(filename, "r") as infile:
         next(infile) 

         for line in infile:
              x, y, z, id = line.split()

              x = float(x)
              y = float(y)
              z = float(z)
              id = float(id)

              #add the values to the list
              data.append((x, y, z, id))


         # give the new data out to use later
         return data

    


def totalMomentum (data):
         #calculate  magnitude of the total momentum of each molecule
         #total momentum = squar root ( x^2 + y^2 + z^2 )
         #check if sum is equal or larger than zero
        
         for x, y, z, id in data :
              if x**2 >= 0 and y**2 >= 0 and z**2 >=  0:
                   calculation = math.sqrt(x**2 + y**2 + z**2)

                   print("The total Momentum of", id, "is", calculation)

#ask user for the file path
filename = input("Enter path of your data file:" )

# open and define data before it can be used in the function totalMomentum
data = openfile(filename)

#alculate the momentum
totalMomentum(data)
    






