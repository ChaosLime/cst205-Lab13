##CST 205 - Lab 13 Problem 1
#Nicholas Saunders
#Mitchell Saunders

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
 file = open(getMediaPath() + fileName, "rt")
 fileTxt = file.read()
 wordsToRemoveFromString = ['Wednesday', 'image', 'unobservable', \
                            'black', 'cosmic abyss', 'dense', 'light', \
                            'years', 'scientific evidence', 'imaginations', \
                            'artists', 'algorithms', 'splashy', 'Christopher Nolan\'s', \
                            'Interstellar', 'real', 'unseeable', 'Shep Doeleman', \
                            'Harvard', 'Astrophysics', 'deep', 'galaxy', 'Messier 87', \
                            'Sauron', 'implacable', 'smoke ring', 'portal', 'intergalactic', \
                            'Virgo', 'sun', 'violent', 'jet']
 fileTxt = replaceWords(fileTxt, wordsToRemoveFromString)

 while '_' in fileTxt:
   print("")# new line
   print(fileTxt)
   while True:
     userInput = requestString("What would you like the next word to be?")
     if len(userInput) > 0:
       if userInput.isalpha():
         #add word to blank
         fileTxt = replaceUnderscoreWithWord(userInput, fileTxt, str(fileTxt).find('_'))
         break
       else:
         print("You must enter a valid with only letters.")
   
 print("\n=====Here is your completed MadLib!=====\n")
 print(fileTxt)
  
def replaceUnderscoreWithWord(userInput, fileTxt, startingIndex):
  underscoreLen = 7 # length defined in replaceWords function
  fileTxt = str(fileTxt).replace('_'*underscoreLen,userInput,1)
  return fileTxt
  
def replaceWords(fileTxt, wordsToRemove):
  newStr = str(fileTxt)
  for word in wordsToRemove:
    #if you change the length of the underscores, then you will need to update getIndexOfUnderscore()
    newStr = str(newStr).replace(word,'_______')
  return newStr

    
    