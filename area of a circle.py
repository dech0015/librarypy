
import math
def calculateAreaOfCircle(radius):
    areaOfCircle = math.pi * radius * radius
    return areaOfCircle

radius = float(input('Please enter the radius of a circle: '))
print("Area of a Circle", calculateAreaOfCircle(radius))

import math
def calculateDistanceBetweenPoints(x,y,x1,y1):
    dist = math.sqrt ((x1-x) ** 2 + (y1-y) ** 2)
    return dist

x = float(input('Please enter x: '))
y = float(input('Please enter y: '))
x1 = float(input('Please enter x1: '))
y1 = float(input('Please enter y1: '))
print(calculateDistanceBetweenPoints(x,y,x1,y1))

def caculateMpg(milesDriven, gallonsOfGasUsed):
    MPG = milesDriven / gallonsOfGasUsed
    return MPG

milesDriven = float( input( "Enter the number of miles driven: " ))
gallonsOfGasUsed = float( input( "Enter the number of gas used: " ))

print( "The car's miles-per-gallon is", caculateMpg(milesDriven, gallonsOfGasUsed))

def convertFahrenheitToCelsius(Fah):
    c = (Fah - 32) * 5 / 9
    return c

Fah = float(input("What is the temperature in Farenheit? "))
print(convertFahrenheitToCelsius(Fah))




