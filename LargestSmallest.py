##Author: Steve Gonzalez
##Date: 09/20/2017
##Class: CIS 1400-003
##Program: Lab 5 Largest and Smallest
##Descr:
##    This program will prompt the user to input
##    a series of numbers of their choosing and
##    will display the largest and smallest of
##    the series of numbers

# A module to describe the function of this program
# to the user
def welcome():
    print('--------------------------------------------')
    print('Welcome! This program allows you to')
    print('input as many numbers as you would')
    print('like and will display the value of')
    print('the largest and smallest numbers that')
    print('you entered. When you have finished')
    print('entering your values, please enter the')
    print('number -99 to indicate the end of your input')
    print('--------------------------------------------')

# A module that will take the largest and smallest values
# from the user input, passed by value, and display each
def displayResults(largest, smallest):
    print('The largest value you entered is: ',largest)
    print('The smallest value you entered is: ',smallest)

# main module that will prompt the user for their list of
# numbers and store the largest and smallest values
def main():
    welcome()
    # variable to store the value entered by the user
    inputNum = float()
    # variables to store the largest and smallest values
    largestNum = float(); smallestNum = float()
    
    inputNum = float(input('Enter a value. If you are \
finished entering values, please enter -99:'))
    if inputNum == -99:
        print('You entered no values.')
    else:
        smallestNum = inputNum
        largestNum = inputNum
        # this loop will continue until the user inputs the
        # number -99. It will compare the input value to the
        # current values of largestNum and smallestNum and
        # reassign the value of each variable as needed
        while inputNum != -99:
            if inputNum > largestNum:
                largestNum = inputNum
            elif inputNum < smallestNum:
                smallestNum = inputNum
            
            inputNum = float(input('Enter a value. If you are \
finished entering values, please enter -99:'))
        
        # call the displayResults module and pass the largest
        # and smallest values as arguments
        displayResults(largestNum,smallestNum)

# begin the program by calling the main module
main()

##Sample output:
##
##--------------------------------------------
##Welcome! This program allows you to
##input as many numbers as you would
##like and will display the value of
##the largest and smallest numbers that
##you entered. When you have finished
##entering your values, please enter the
##number -99 to indicate the end of your input
##--------------------------------------------
##Enter a value. If you are finished entering values, please enter -99:-99
##You entered no values.
##>>> main()
##--------------------------------------------
##Welcome! This program allows you to
##input as many numbers as you would
##like and will display the value of
##the largest and smallest numbers that
##you entered. When you have finished
##entering your values, please enter the
##number -99 to indicate the end of your input
##--------------------------------------------
##Enter a value. If you are finished entering values, please enter -99:8
##Enter a value. If you are finished entering values, please enter -99:55
##Enter a value. If you are finished entering values, please enter -99:2
##Enter a value. If you are finished entering values, please enter -99:0
##Enter a value. If you are finished entering values, please enter -99:21
##Enter a value. If you are finished entering values, please enter -99:-99
##The largest value you entered is:  55.0
##The smallest value you entered is:  0.0
