import math

def openfile(filename):
    # create an empty list to then add the data points from the file into it
    data = []

    with open(filename, "r") as infile:
        next(infile)

        for line in infile:
            values = line.split()

            # check if each line has 4 values in the file
            if len(values) != 4:
                print("Error: Each line needs to contain four values in a txt file")
                continue

            # check if each value is a number
            try:
                x = float(values[0])
                y = float(values[1])
                z = float(values[2])
                id = float(values[3])

            except ValueError:
                print("Error: value must be a number")
                continue

            # add the values to the list
            data.append((x, y, z, id))

    # give the new data out to use later
    return data


def totalMomentum (data):
         #calculate  magnitude of the total momentum of each molecule
         #total momentum = squar root ( x^2 + y^2 + z^2 )
         
         
         for x, y, z, id in data :
              #check if sum is equal or larger than zero
              if x**2 >= 0 and y**2 >= 0 and z**2 >=  0:
                   #then calculate the momentum 
                   calculation = math.sqrt(x**2 + y**2 + z**2)

                   print("The total Momentum of", id, "is", calculation)

#ask user for the file path
filename = input("Enter path of your data file:" )

# open file and define data as the input form user before it can be used in the function totalMomentum
data = openfile(filename)

#alculate the momentum
totalMomentum(data)
    






