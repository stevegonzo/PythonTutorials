##Author: Steve Gonzalez
##Date:   10/02/2017 Optimized 10/04/2017 (SJG)
##Class:  CIS 1400-3
##Prog:   Lab #6 Test Average and Grade
##Desc:
##    This program uses multiple functions to prompt the user
##    for 5 test scores and then displays the corresponding
##    letter grade for each score and the average of the test
##    scores. It uses validation functions to ensure the user
##    enters valid input

def main():
    # local variables intialized with getValidScore
    score1 = getValidScore()
    score2 = getValidScore()
    score3 = getValidScore()
    score4 = getValidScore()
    score5 = getValidScore()
    # display each score and the corresponding letter grade
    print('-----', '\t', '-----')
    print('SCORE', '\t', 'GRADE')
    print('-----', '\t', '-----')
    print(score1, '\t', determineGrade(score1))
    print(score2, '\t', determineGrade(score2))
    print(score3, '\t', determineGrade(score3))
    print(score4, '\t', determineGrade(score4))
    print(score5, '\t', determineGrade(score5))

    # call calcAverage to determine the average score
    scoreAverage = calcAverage(score1, score2, score3, score4, score5)

    # display the average score
    print('The average test score is: ', scoreAverage)

# Function Name: isValidScore
# Parameters:    testScore as a string
# Returns:       True if test score is valid; False otherwise
# Description
# The isValidScore function determines if the input test score
# is a numeric value in the range of 0 to 100         
def isValidScore(testScore):
    isValid = False # boolean flag
    # check for valid floating point string
    if not testScore.replace('.', '', 1).isnumeric() or \
       (float(testScore) < 0 or float(testScore) > 100):
        isValid = False
    else:
        isValid = True

    return isValid

# Function Name: getValidScore
# Parameters:    NONE
# Returns:       test score as real
# Description
# The getValidScore function prompts and reads a test score
# from the user and returns it. Uses validation loop to ensure
# the user entered a valid test score
def getValidScore():
    # local variable to hold test score
    validTestScore = ''
    # get the test score
    validTestScore = input('Enter a test score. Valid test scores \
are between 0 and 100: ')
    # validation loop
    while not isValidScore(validTestScore):
          validTestScore = input('You entered an invalid score. \
Please enter a NUMERIC score between 0 and 100: ')
    return float(validTestScore)

# Function Name: calcAverage
# Parameters:    Five test scores as real
# Returns:       average test score as real
# Description
# The calcAverage function takes five test scores a parameters
# and divides the total of all scores by the number of scores
# and returns the average
def calcAverage(score1, score2, score3, score4, score5):
    # local named constant for the number of scores
    NUM_SCORES = int(5)
    # add the scores together and store them in the total variable
    total = score1 + score2 + score3 + score4 + score5
    # calculate the average score
    average = total / NUM_SCORES
    return average

# Function Name: determineGrade
# Parameters:    test score as real
# Returns:       letter grade a string
# Description
# The determineGrade function uses mulitple alternative
# decision structure to determine the corresponding letter
# grade for the test score passed in as a parameter and returns
# the letter grade
def determineGrade(testScore):
    if testScore <= 100 and testScore >= 90:
          letterGrade = 'A'
    elif testScore <= 89 and testScore >= 80:
          letterGrade = 'B'
    elif testScore <= 79 and testScore >= 70:
          letterGrade = 'C'
    elif testScore <= 69 and testScore >= 60:
          letterGrade = 'D'
    else:
          letterGrade = 'F'

    return letterGrade

# start the program by calling the main module
main()

##Sample Output:
##    >>> main()
##Enter a test score. Valid test scores are between 0 and 100: eighty
##You entered an invalid score. Please enter a NUMERIC score between 0 and 100: 80
##Enter a test score. Valid test scores are between 0 and 100: -25
##You entered an invalid score. Please enter a NUMERIC score between 0 and 100: 90
##Enter a test score. Valid test scores are between 0 and 100: 110.0
##You entered an invalid score. Please enter a NUMERIC score between 0 and 100: 80.0
##Enter a test score. Valid test scores are between 0 and 100: -5
##You entered an invalid score. Please enter a NUMERIC score between 0 and 100: 90
##Enter a test score. Valid test scores are between 0 and 100: 85.0
##----- 	 -----
##SCORE 	 GRADE
##----- 	 -----
##80.0 	 B
##90.0 	 A
##80.0 	 B
##90.0 	 A
##85.0 	 B
##The average test score is:  85.0
