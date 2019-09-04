##Author: Steve Gonzalez
##Date: 09/14/2017
##Class: CIS 1400-003
##Program: Lab 4 - Shipping Charge
##Descr:
##    This program will calculate the
##    shipping charge for a package when
##    the user enters a weight

# main module that starts the program and asks
# the user to input the package weight
def main():
    weight = float(input('Enter the weight of the package: '))
    calcAndDisplayShipping(weight)

# define module that will calculate the shipping
# charge and display the result
def calcAndDisplayShipping(weight):
    # local named constants to represent the
    # shipping rate for each weight interval
    TWO_LB_RATE = 1.1
    TWO_TO_SIX_LB_RATE = 2.2
    SIX_TO_TEN_LB_RATE = 3.7
    TEN_LB_RATE = 3.8
    # local variable to hold value of shipping charge
    # initialized to represent Real number type
    shippingCharge = 0.0
    # a set of conditional statements to determine the
    # shipping charge based on the weight passed by value
    if weight <= 2.0 and weight >=0:
        shippingCharge = round(weight * TWO_LB_RATE,2)
    elif weight > 2.0 and weight <= 6.0:
        shippingCharge = round(weight * TWO_TO_SIX_LB_RATE,2)
    elif weight > 6.0 and weight <= 10.0:
        shippingCharge = round(weight * SIX_TO_TEN_LB_RATE,2)
    elif weight > 10.0:
        shippingCharge = round(weight * TEN_LB_RATE,2)
    else:
        shippingCharge = 0.0
        print('An invalid weight was entered.')
    # display the shipping charge
    print('The shipping charge for your package is: $', shippingCharge)

#run the main module to start the program
main ()

## Sample output
##Enter the weight of the package: 1.3
##The shipping charge for your package is: $ 1.43
##>>> main()
##Enter the weight of the package: 2
##The shipping charge for your package is: $ 2.2
##>>> main()
##Enter the weight of the package: 3.5
##The shipping charge for your package is: $ 7.7
##>>> main()
##Enter the weight of the package: 6
##The shipping charge for your package is: $ 13.2
##>>> main()
##Enter the weight of the package: 7.5
##The shipping charge for your package is: $ 27.75
##>>> main()
##Enter the weight of the package: -1
##An invalid weight was entered.
##The shipping charge for your package is: $ 0.0
##>>> 
