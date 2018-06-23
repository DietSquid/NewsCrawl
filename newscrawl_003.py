#NewsCrawl
#Designed to display a feed of headlines from the subreddit of one's choice
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import os
import sys
from screeninfo import get_monitors

#number of seconds each headline will be displayed
delay = 15

def main():
    while True:
        newsrequest()
        #opening the profile data in a variable
        hubworld = hub.read()
        hub.close()
        #calls the parser and grabs all the relevant links on the page
        parsehub = soup(hubworld, "html.parser")
        entries = (parsehub.findAll("div",{"class":"top-matter"},
                               {"p class":"title"}))
        #run display function for every headline
        global ghg
        for ghg in entries:
            display()


def request():
    os.system('cls' if os.name == 'nt' else 'clear')

    #Determine the subreddit to direct to, first by checking if any was given,
    #and then choosing the default
    print(sys.argv)
    if len(sys.argv) > 1:
        sub = sys.argv[1]       #set sub in url, *only* if it is specified
    else:
        sub = 'worldnews'
    global url
    url = ('https://reddit.com/r/' + sub)
    print ("NewsCrawl ver. 0.4")
    print('Attempting to reach', url, '...')      #just for debug purposes
    newsrequest()

def newsrequest():
    while True:
        try:
            global hub
            #urlopen function using profile
            hub = uReq(url)
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('ERROR: Too many requests! ' +
                  'Program is having difficulty connecting to reddit. ' +
                  'The program will retry to connect in a few seconds.')
            time.sleep(2)
            continue
        break


def display():
    os.system('cls' if os.name == 'nt' else 'clear')
    #getting the window dimensions and putting the text in the center
    rows, columns = os.popen('stty size', 'r').read().split()
    rowuse = len(ghg.a.text) / int(columns)
    spacing = (int(rows) / 2) - (int(rowuse) / 2)
    lin = int(spacing)
    for spaces in range(lin):
        print(" ")
    scrolling(ghg.a.text, columns)  #print the headline
    time.sleep(delay)   #delay before moving down the list


def scrolling(strng, rowlngth):
    scrlength = 0
    #split the headline into individual characters.
    #This is so we can incorporate a text scrolling function
    #and better detect when to split the string when we reach a line break
    for letter in strng:
        #if there's no room left on the row, new line, print first letter
        if scrlength == rowlngth:
            print('\n', letter, end='', flush = True)
            scrlength = 0
        else:
            print(letter, end='', flush = True)  #print letter
            scrlength += 1
            time.sleep(.007)


request()                                                                       #getlink
main()                                                                          #run loop program
