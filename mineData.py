'''
to generate C2:
        Input:
            [ ["A"], ["B"], ["C"], ["D"] ]
        Output:
            [ ["A", "B"], 2, ["A", "C"], 1, ["A", "D"], 2, ["B", "C"], 3, ["B", "D"], 2, ["C", "D"], 4, ]
to generate C3:
        Input:
            [ ["A", "B", "D"], ["B", "C", "D"] ]
        Output:
            [ ["B", "C", "D"], 2 ]
####################################################


'''


'' ''''''''''''''''''''''''''''
    #   Definition section states
'' '''''''''''''''''''''''''''''
#   This function generates FrequentSets and stroes them in an array
def generateFrequentItemSet(CandidateList, noOfTransactions, minimumSupport):
    returnArray = []
    for i in range(len(CandidateList)):
        if i%2 != 0:
            support = (CandidateList[i] * 1.0 / noOfTransactions) * 100
            if support >= minimumSupport:
                returnArray.append(CandidateList[i-1])
                returnArray.append(CandidateList[i])
            else:
                eleminatedItemsArray.append(CandidateList[i-1])
    return returnArray

#   This function creates Candidate set C1 from the given data set
def generateC1(dataSet):
    itemDict = {}
    for line in dataSet:
        for word in line:
            if word not in itemDict:
                itemDict[word] = 1
            else:
                itemDict[word] = itemDict[word] + 1
    return itemDict

#   This function generates and return L1 from
def generateL1(itemDict, minimumSupport, noOfTransactions):
    returnDict = {}

    for key in itemDict:
        tempValue = itemDict[key]
        tempSupport = (tempValue * 1.0 / noOfTransactions) * 100
        if tempSupport >=minimumSupport:
            returnDict[key] = itemDict[key]
        else:

    return returnDict

#   This function creates Candidate set C2 from the given data dataSet
def generateC2(l1Dict):
    tempArray = []
    returnArray = []
    for key in l1Dict:
        tempArray.append(key)
    for item in tempArray:
        tempItemList = []
        k = tempArray.index(item)
        for i in range(k + 1, len(tempArray)):
            tempItemList.append(item)
            tempItemList.append(tempArray[i])
            returnArray.append(tempItemList)
            tempItemList = []
    return returnArray

'' ''''''''''''''''''''''''''''
    #   Definition section ends
'' '''''''''''''''''''''''''''''

# using case, set up the file name value
fileName = "computerStuff.txt"

# defining values for minimum support and minimum confidence
minimumSupport = 48
minimumConfidence = 70

#   Array to store the non frequent sets
nonFrequentSets = []

# Read the data line by line from the file and store in a list
with open(fileName) as fp:
    lines = fp.readlines()

# Split the items with the , delimeter
dataSet = []
for line in lines:
    line = line.rstrip()
    dataSet.append(line.split(","))

#   Storing the number of transactions
noOfTransactions = len(dataSet)

# create a dictionary of unique items from the nexted list
itemDict = generateC1(dataSet)

# Create a list of unique items in the dataSet
uniqueItems = []
for key in itemDict:
    uniqueItems.append(key)

# Eleminate the candidates which are less than minimumSupport
l1Dict = generateL1(itemDict, minimumSupport, noOfTransactions)

#
c2Dict = generateC2(l1Dict)













'''
#   Printing to test stuff
print("\n")
print("Dataset")
for i in dataSet:
    print(i)

print("\n")
print("Non frequent sets")

print("\n")
print("Unique Items: " + str(uniqueItems))

print("\n")
print("C1: " + str(itemDict))

print("\n")
print("L1: " + str(l1Dict))

print("\n")
print("C1: ")
for i in c2Dict:
    print(i)
'''