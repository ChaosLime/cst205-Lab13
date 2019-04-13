##CST 205 - Lab 13 Problem 1
#Nicholas Saunders
#Mitchell Saunders

#Mad Libs are a classic party game where you start with a story with some of the words removed.
#requirments: 
#    inputs:supply words, without knowing what the story is about.
#(by part of speech, names, numbers, etc)
#    outputs:words supplied, inserted into story and is "read aloud"

#Step 1: Find a news article online
#You only need between 100 and 200 words for a decent mad lib, 
#so if you find a really long story, take only part of it. 

##Article used: https://www.nytimes.com/2019/04/10/science/black-hole-picture.html?module=inline
##Text file for ~200words in BlackHole.txt

#Step 2: Remove some words
#Go through the article and turn it into strings in Python and remove some of the words.
#These will be the words that become part of the Mad Lib Game

#Step 3: Make some design decisions
#You need to think about how you are going to ask the user to enter the words,
#how you are going to store the words entered, and how you are going to print out the restulting story.
#There are several different ways to accomplish this using strings and lists.  
#The one rule is that you cannot use a separate variable for every word you need.

#Step 4: Collect words from the user
#Prompt the user to enter the words that you need to fill in your mad lib 

#Step 5: Print the results
#Combine the original text plus the new words to print your final mad lib.

########################### Start of File
import os #to allow access to os.path.abspath(__file__) and os.path.dirname

def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')
    
def madLib():
 setMediaPathToCurrentDir()
 ##reads file, then breaks characters into words
 fileName = "BlackHole.txt"
 file = open(setMediaPath() + fileName,"rt")
 words = file.read().split(' ') 
 
 #puts words into list
 wordsInList = []
 for i in words:
   wordsInList.append(i)
 #print wordsInList
 print cleanUpList(wordsInList)
 
 #once cleaned up, remove words and record their index
 #collect list of words from user
 #print results
 
def cleanUpList(list):
  return str(list).replace('[','').replace(']','').replace(',','').replace('\'','').replace(r'\n','\n')
  # cleans up text, yet removes ',' char from phrasing and words.
 

    
    