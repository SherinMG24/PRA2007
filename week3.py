import math

def openfile(filename):
    # create an empty list to then add the data points from the file into it
    data = []

    with open(filename, "r") as infile:

        for line in infile:
            values = line.split()


            # check if each line has 4 numbers and no letters, then add to the list 
            if len(values) == 4:
                try:
                    x = float(values[0])
                    y = float(values[1])
                    z = float(values[2])
                    id = float(values[3])
                except ValueError:
                                print("Error: value must be a number")
                                continue
                data.append((x, y, z, id)) 

            #check if a line has 2 numbers and no letters, then add to the list
            elif len(values) == 2:
                try:
                    NumberofEvent = float(values [0])
                    MoleculesinEvent = float (values [1])
                except ValueError:
                                print("Error: value must be a number")
                                continue
                data.append((NumberofEvent, MoleculesinEvent))

            else :
                print("Error: Line has invalid imput")


    # give the new data out to use later
    return data

#count just the numbers of events, that need to be considered (where Molecules were reported)
def countEvents(data):
    #start with 0 and then add 1 for each event, where Molecules in Event is not zero
    TotalNumber = 0

    for values in data:
        #so it only reads the lines with 2 values (headers)
        if len(values) == 2:
            NumberofEvent, MoleculesinEvent = values
            # add 1 to the TotalNumber count, if the Molecules in the event is not zero
            if MoleculesinEvent != 0:
                TotalNumber += 1

    #give the number out, so it can be used in later calculations
    return TotalNumber

#count Moleules per ID
def countMolecules(data, IDnumber):
    ##start with 0 and then add 1 for each event with the same ID number
    MoleculeNumber = 0

    for values in data:
          if len(values) == 4:
                x, y, z, id = values

                if id == IDnumber:
                    MoleculeNumber += 1

   #give the number out, so it can be used in later calculations
    return MoleculeNumber

#calucate the average by deviding the Number of one ID by the total amount of events
def average (MoleculeNumber, TotalNumber):
      # check that TotalNUmber is not zero
      if TotalNumber != 0:
            averageEvent = MoleculeNumber/ TotalNumber
            #check that averageEvent is not negative
            if averageEvent >= 0:
                standartDevidation = math.sqrt(averageEvent)  
            

      print("The molecule with the ID",IDnumber,"has an average and standard deviation of: ", averageEvent, "+/-", standartDevidation)

      
#ask user for the file path
filename = input("Enter path of your data file:" )

# open file and define data as the input form user before it can be used in the next functions 
data = openfile(filename)

#define TotalNumber, so that it can be used in the next function
TotalNumber = countEvents (data)

# list of all the possible IDs
IDs = [211, -211, 321, -321, 2212, -2212, 3122, -3122, 3312, -3312, 3334, -3334]

# run the average function for every possible ID
for IDnumber in IDs :
    #define MoleculeNumber, so that is can be used in the next function
    MoleculeNumber = countMolecules (data, IDnumber)
    #calculate avergae of ID
    average (MoleculeNumber, TotalNumber)



