##Author: Steve Gonzalez
##Class:  CIS 1400-003
##Date:   11/30/2017
##Prog:   Lab #11 - Property Tax GUI
##Descr:
##    This program uses a GUI approach to prompt the user
##    for the value of a property. The program then calculates
##    the assessed value and property tax and displays the
##    results in the GUI

# import Tkinter classes
from tkinter import *

# class to create the GUI
class PropTax_GUI:
    # constructor
    def __init__(this):
        # create window
        this.mainWindow = Tk()
        this.mainWindow.title('Property Tax Calculator')
        this.mainWindow.geometry('450x140')

        # create labels and text boxes
        # row 0
        this.valueLabel = Label(this.mainWindow, \
                                text = 'Enter the Value of the Property:')
        this.propValueTextBox = Entry(this.mainWindow, width = 15)
        this.valueLabel.grid(row = 0, column = 0)
        this.propValueTextBox.grid(row = 0, column = 1)
        # row 1
        this.assessmentLabel = Label(this.mainWindow, \
                                     text = 'Assessment Value:')
        this.assessValueLabel = Label(this.mainWindow, \
                                      text = '')
        this.assessmentLabel.grid(row = 1, column = 0)
        this.assessValueLabel.grid(row = 1, column = 1)
        # row 2
        this.taxLabel = Label(this.mainWindow, \
                              text = 'Property Tax:')
        this.propTaxLabel = Label(this.mainWindow, \
                                  text = '')
        this.taxLabel.grid(row = 2, column = 0)
        this.propTaxLabel.grid(row = 2, column = 1)
        # create buttons for action events
        this.calcButton = Button(this.mainWindow, \
                                 text = 'Calculate Assessment Value & Property Tax', \
                                 command = this.calcButton_Click)
        this.exitButton = Button(this.mainWindow, \
                                 text = 'Exit', fg = 'red', \
                                 command = this.mainWindow.destroy)
        this.calcButton.grid(row = 3, column = 0)
        this.exitButton.grid(row = 3, column = 1)

        # enter the main processing loop
        this.mainWindow.mainloop()

    # event handler for calcButton
    def calcButton_Click(this):
        # named constants
        ASSESSED_PERCENT = 0.6
        TAX_RATE = 0.0064
        # get property value
        propValue = float(this.propValueTextBox.get())
        # calculate assessment value
        assessValue = propValue * ASSESSED_PERCENT
        # calculate property tax
        propTax = assessValue * TAX_RATE
        # display results
        this.assessValueLabel.configure(text = '$' + format(assessValue, '.2f'))
        this.propTaxLabel.configure(text = '$' + format(propTax, '.2f'))
        

# main module to control program run
def main():
    # create instance of PropTax_GUI class
    myPropTax = PropTax_GUI()

# start program by calling main
main()
    
        
