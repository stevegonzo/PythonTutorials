##Author: Steve Gonzalez
##Class:  CIS 1400-003
##Date:   10/18/2017
##Prog:   Lab #7 - Rainfall Statistics
##Descr:
##    Program that prompts the user for rainfall totals for
##    each month of the year. Those totals are stored in an
##    array with a parallel array for the corresponding months.
##    The program then displays that total annual rainfall, the
##    monthly average rainfall, the month with the lowest
##    rainfall, and the month with the highest rainfall.

def main():
    # constant Integer for array size
    SIZE = 12
    # parallel arrays for months and rainfall statistics
    months = ['January', 'February', 'March', 'April', \
              'May', 'June', 'July', 'August', 'September', \
              'October', 'November', 'December']
    rainfallStats = [0] * SIZE
    # local variables for average and total rainfall
    average = float(); total = float()
    # local variables for index of lowest and highest rainfall
    lowIndex = int(); highIndex = int()

    # call getRainfall to initialize rainfallStats array
    getRainfall(rainfallStats, months, SIZE)

    print('--------------------------------------')

    # set total with getTotal function
    total = getTotal(rainfallStats, SIZE)
    # display total
    print('The total annual rainfall is', total, 'inches.')

    # set average with getAverage function
    average = getAverage(total, SIZE)
    # display average
    print('The average monthly rainfall is', average, 'inches.')

    # set lowIndex with getSmallestRainfall function
    lowIndex = getSmallestRainfall(rainfallStats, SIZE)
    # display lowest rainfall month
    print('The lowest rainfall total occurred in', months[lowIndex])
    print('The total rainfall that month is', rainfallStats[lowIndex], 'inches.')

    # set highIndex with getLargestRainfall function
    highIndex = getLargestRainfall(rainfallStats, SIZE)
    # diplay highest rainfall month
    print('The highest rainfall total occurred in', months[highIndex])
    print('The total rainfall that month is', rainfallStats[highIndex], 'inches.')


def getRainfall(rainfall, months, arraySize):
    # loop counter
    index = int()

    #for loop to get rainfall stats from user
    for index in range(0, arraySize):
        rainfall[index] = float(input('Enter rainfall total for ' + months[index] + ' in inches: '))

def getTotal(array, arraySize):
    # loop counter
    index = int()
    # accumulator
    total = float()

    # for loop to total array elements
    for index in range(0, arraySize):
        total = total + array[index]
    # return total
    return total

def getAverage(total, numInputs):
    # local variable for average
    average = float()
    # calculate average
    average = total / numInputs
    # return average
    return round(average, 2)

def getSmallestRainfall(array, arraySize):
    # local variable to hold lowest rainfall value
    lowest = array[0]
    # local variable to hold index of lowest rainfall element
    lowIndex = int()
    # loop counter
    index = int()

    #step through remaining array
    for index in range(1, arraySize):
        if array[index] < lowest:
            lowest = array[index]
            lowIndex = index

    # return index of lowest value
    return lowIndex

def getLargestRainfall(array, arraySize):
    # local variable to hold highest rainfall value
    highest = array[0]
    # local variable to hold index of highest rainfall element
    highIndex = int()
    # loop counter
    index = int()

    # step through remaining array
    for index in range(1, arraySize):
        if array[index] > highest:
            highest = array[index]
            highIndex = index

    # return index of highest value
    return highIndex
        
# start the program by calling main module
main()

##SAMPLE OUTPUT:
##Enter rainfall total for January in inches: 1.5
##Enter rainfall total for February in inches: 2.5
##Enter rainfall total for March in inches: 3.5
##Enter rainfall total for April in inches: 8
##Enter rainfall total for May in inches: 9.1
##Enter rainfall total for June in inches: 12.1
##Enter rainfall total for July in inches: 4.2
##Enter rainfall total for August in inches: 15
##Enter rainfall total for September in inches: 12.25
##Enter rainfall total for October in inches: 9.5
##Enter rainfall total for November in inches: 1.5
##Enter rainfall total for December in inches: 0.5
##--------------------------------------
##The total annual rainfall is 79.65 inches.
##The average monthly rainfall is 6.64 inches.
##The lowest rainfall total occurred in December
##The total rainfall that month is 0.5 inches.
##The highest rainfall total occurred in August
##The total rainfall that month is 15.0 inches.
