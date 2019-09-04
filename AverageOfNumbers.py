##Author: Steve Gonzalez
##Date:   10/23/2017
##Prog:   Lab #8 - Average of Numbers
##Descr:
##    This program reads integers from numbers.dat file
##    and calculates and displays the average of all
##    numbers read

def main():
    # local variables to hold each number read,
    # a counter for the number of integers read
    # from the list, the total, and the average
    num = int(); counter = int(); total = int(); average = float()

    # declare and open the input file
    numbersFile = open('numbers.dat', 'r')

    # read line from file
    line = numbersFile.readline()

    # read integers from file and total them
    # increment counter each time an integer is read
    while line != '':
        num = int(line)
        total = total + num
        counter = counter + 1
        # read the next line
        line = numbersFile.readline()

    # close the file
    numbersFile.close()

    # calculate the average
    average = format(total / counter, '.2f')

    # display the average
    print('The average of the numbers read from the file is:', average)

# start program by calling main module
main()

        
##SAMPLE OUTPUT:
##
##The average of the numbers read from the file is: 59.29
