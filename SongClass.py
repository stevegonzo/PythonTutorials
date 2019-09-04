##Author: Steve Gonzalez
##Class:  CIS 1400-003
##Date:   11/16/2017
##Prog:   Lab #10 - Song Class
##Descr:
##    This program defines the Song Class and prompts
##    the user for data to create two instances of the
##    Song class. The fields of those objects are then
##    written to file using accessor methods.

class Song:
    # constructor
    def __init__(this, art, ttle, tme, yr):
        this.__artist = art
        this.__title = ttle
        this.__time = tme
        this.__year = yr

    # mutator methods
    def setArtist(this, art):
        this.__artist = art
    def setTitle(this, ttle):
        this.__title = ttle
    def setTime(this, tme):
        this.__time = tme
    def setYear(this, yr):
        this.__year = yr

    # accessor functions
    def getArtist(this):
        return this.__artist
    def getTitle(this):
        return this.__title
    def getTime(this):
        return this.__time
    def getYear(this):
        return this.__year

# main module
def main():
    # local variables to store user input
    artist1 = ''; artist2 = ''
    title1 = ''; title2 = ''
    time1 = float(); time2 = float()
    year1 = int(); year2 = int()

    # prompt user for input
    print('Create library information for songs by entering the requested data')
    print()
    print('Enter the song information for song #1')
    artist1 = input('Artist Name: ')
    title1 = input('Track Title: ')
    time1 = float(input('Track Length(minutes): '))
    year1 = int(input('Release Year: '))
    print()

    
    print('Enter the song information for song #2')
    artist2 = input('Artist Name: ')
    title2 = input('Track Title: ')
    time2 = float(input('Track Length(minutes): '))
    year2 = int(input('Release Year: '))

    # create Song objects from user input
    song1 = Song(artist1, title1, time1, year1)
    song2 = Song(artist2, title2, time2, year2)

    # open a file for output
    songFile = open('song_inventory.dat', 'w')

    # write data to file
    songFile.write('Song #1: ' + song1.getArtist() +', '+ song1.getTitle()+ ', ' +\
                    str(song1.getTime())+', ' + str(song1.getYear())+'\n')
    songFile.write('Song #2: ' + song2.getArtist() +', '+ song2.getTitle()+ ', ' +\
                    str(song2.getTime())+', '+ str(song2.getYear()))
    print('-------------------')
    print('Data written to file.')


# begin program by calling main
main()

##SAMPLE PROGRAM RUN:
##Create library information for a song by entering the requested data
##
##Enter the song information for song #1
##Artist Name: Coldplay
##Track Title: Paradise
##Track Length(minutes): 4.39
##Release Year: 2011
##
##Enter the song information for song #2
##Artist Name: Imagine Dragons
##Track Title: On Top of the World
##Track Length(minutes): 3.12
##Release Year: 2012
##-------------------
##Data written to file.
