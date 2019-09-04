##Author: Steve Gonzalez
##Date:   11/02/2017
##Class:  CIS 1400-003
##Prog:   Lab #9 - Sort/Search Names
##Descr:
##    This program creates an array of Strings that contains
##    various names. The list is then sorted alphabetically
##    using a bubble sort and displayed to the user. The user
##    is prompted to search for a name and the program uses
##    a binary search to find it.

def main():
    # named constant for array size
    SIZE = int(10)
    # local variable to hold search item
    searchValue = ''
    # local variable to hold index of found item
    searchIndex = int()
    # initialize String array
    names = ['Ross Harrison', 'Hannah Beauregard', 'Bob White',\
             'Ava Fischer', 'Chris Rich', 'Xavier Adams',\
             'Sasha Ricci', 'Danielle Porter', 'Gordon Pike', \
             'Matt Hoyle']

    # call bubble sort module to sort names array in ascending order
    bubbleStrSort(names, SIZE)

    # display the sorted array
    displayStrArray(names, SIZE)

    # call getSearchName function to prompt the user for search item
    searchValue = getSearchName()

    # call search function to determine location of the searched name
    # in the array. Will return -1 if the name was not found
    searchIndex = binaryStrSearch(names, SIZE, searchValue)

    # condition statement to determine if the searched name was found
    if searchIndex != -1:
        print('The name you searched for was found in element', searchIndex)
    else:
        print('-------------------------------------------------')
        print('|ERROR! The name you searched for was not found.|')
        print('-------------------------------------------------')


# Module Name: bubbleStrSort
# Parameters:  String array and Int for size of array
# Descr:       This module accepts a string array and sorts
#              the contents in ascending (alphabetical) order.
#              It uses case-insensitive for comparisons for
#              the array elements
def bubbleStrSort(array, arraySize):
    # maxElement will contain the subscript of the last
    # element needed to be compared
    maxElement = int()
    # counter variable for loop
    index = int()

    # outer loop to position maxElement as the array is sorted
    for maxElement in range(arraySize - 1, -1, -1):
        # inner loop to step through array to maxElement
        for index in range(0, maxElement):
            # compare the element to the next and swap if necessary
            if array[index].upper() > array[index + 1].upper():
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp

# Module Name: displayStrArray
# Paramters:   String array and Int for size of array
# Descr:       This module accepts a String array and
#              displays a message to the user describing
#              the data. A for loop steps through the array
#              and displays the contents
def displayStrArray(array, arraySize):
    # counter variable for loop
    index = int()
    print()
    print('Below are the names sorted in alphabetical order:')
    # display contents of array
    for index in range(0, arraySize):
        print(array[index])

# Function Name: getSearchName
# Parameters:    NONE
# Returns:       User input as String
# Descr:         getSearchName prompts the user for a name that
#                will be used in a later search. The input is
#                in a String variable which is returned to the
#                function call statement
def getSearchName():
    # local variable to store user input
    searchName = ''
    print()
    # prompt the user for name to search for
    searchName = input('Enter the name that you would like to search for: ')
    return searchName

# Function Name: binaryStrSearch
# Parameters:    A SORTED String array, Int representing array size
#                and a String to search for
# Returns:       The position (subscript) of the element containing
#                the search item as an Int or -1 if the item was
#                not found
# Descr:         This function finds the midpoint of the parameter array
#                and then compares the value at the midpoint element to the
#                search item. If the search item was found at the midpoint
#                the function returns that position. Otherwise, the
#                function looks in the first half of the array if the search
#                item is less than the midpoint item, or in the second half
#                of the array if the search item is greater than the midpoint
#                item. This recurs until the search item is found or the entire
#                array has been search. Uses case-insensitive String comparisons.
def binaryStrSearch(array, arraySize, searchValue):
    # local variable to hold the subscript of the first element to search
    first = int(0)
    # local variable to hold the subscript of the last element to search
    last = arraySize - 1
    # local variable to hold the position of the search item
    position = -1
    # Boolean flag
    found = False
    # local variable to gold the subscript of the midpoint
    middle = int()

    # loop while search value not found and the entire array hasn't been searched
    while (not found) and (first <= last):
        # calculate midpoint
        middle = int((first + last) / 2)

        #check midpoint for search value
        if array[middle].upper() == searchValue.upper():
            found = True
            position = middle
        # check lower half
        elif array[middle].upper() > searchValue.upper():
            last = middle - 1
        # if not in lower half, check upper half
        else:
            first = middle + 1

    return position

# start program by calling main module
main()

##SAMPLE OUTPUT:
##    Below are the names sorted in alphabetical order:
##Ava Fischer
##Bob White
##Chris Rich
##Danielle Porter
##Gordon Pike
##Hannah Beauregard
##Matt Hoyle
##Ross Harrison
##Sasha Ricci
##Xavier Adams
##
##Enter the name that you would like to search for: bob white
##The name you searched for was found in element 1
##>>> 
