import random

computerStuff = ["Desktop", "Laptop", "Mouse", "Keyboard", "Printer", "HDMI", "SSD", "HDD", "Monitor", "Processor"]
candies = ["AlmondJoy", "KitKat", "HeathBar", "BabyRuth", "Twix", "Snickers", "Cotton Candy", "MilkyWay", "Hershey", "Cadbury"]
mobileStuff = ["HeadPhones", "Charger", "Splitter", "Lences", "Battery", "Processor", "HomeButton", "Speakers", "Camera", "Screen"]
food = ["Bread", "Milk", "Eggs", "Tea", "Coffee", "Cream", "Bagel", "Sugar", "CreamCheese", "Cheese"]
automobile = ["SideLight", "HeadLight", "Engine", "SteeringWheel", "WindShield", "Oil", "BreakPad", "Wheels", "Tires", "Car"]

selected = []

#File 1
file = open('computerStuff.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(computerStuff[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

#File 2
file = open('candies.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(candies[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

#File 3
file = open('mobileStuff.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(mobileStuff[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

#File 4
file = open('food.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(food[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

#File 5
file = open('automobile.txt' ,'a') 
file.truncate()
for j in range(25):
    for x in range(10):
        selected.append(automobile[random.randint(0,9)])
    selected = set(selected)
    selected = list(selected)
    for i in range(len(selected)):
        if i != len(selected) - 1:
            file.write(selected[i] + ',')
        else:
            file.write(selected[i])
    selected = []
    file.write('\n')  

