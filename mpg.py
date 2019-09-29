def caculateMpg(milesDriven, gallonsOfGasUsed):
    MPG = milesDriven / gallonsOfGasUsed
    return MPG

milesDriven = float( input( "Enter the number of miles driven: " ))
gallonsOfGasUsed = float( input( "Enter the number of gas used: " ))

print( "The car's miles-per-gallon is", caculateMpg(milesDriven, gallonsOfGasUsed))


















