import math
def calculateDistanceBetweenPoints(x,y,x1,y1):
    dist = math.sqrt ((x1-x) ** 2 + (y1-y) ** 2)
    return dist

x = float(input('Please enter x: '))
y = float(input('Please enter y: '))
x1 = float(input('Please enter x1: '))
y1 = float(input('Please enter y1: '))
print(calculateDistanceBetweenPoints(x,y,x1,y1))

/Users/atchimadechaphan/PycharmProjects/python week 4/calculateDistanceBetweenPoints.py
