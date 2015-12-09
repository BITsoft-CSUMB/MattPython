# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------
# The ultimate Madlib game for CST205
# Written by: Ashley Wallac and Matt Valancy (Crenshaw)

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Function header template   -----------------------------------
# ------------------------------------------------------------------------------------------------------------
# Function: What does it do
# Params: What does it accept
# Returns: What does it return

#def printNow(string):
#   print(string)  


rawString = ["WASHINGTON-Sitting Indian-style on the ",
             " floor surrounded by Magic Markers, and ",
             " paper, members of Congress spent ",
             " in a special session Monday drawing ",
             " of their ",
             " Capitols, sources reported. The drawings-which variously featured huge ",
             " affixed to the Capitol dome, a moat ",
             "  with crocodiles and ",
             ", and a ",
             " version of Sen. Marco Rubio (R-FL) that can ",
             " on bills when the senator himself is ",
             " -were reportedly part of an activity devised by congressional ",
             " to alleviate some of the stress caused by ",
             " bipartisan squabbling and to keep the lawmakers ",
             " until recess."]
            
# ------------ STORY TEXT FOR REFERENCE ----------------             
#WASHINGTON—Sitting Indian-style on the ___(noun) floor surrounded by Magic Markers, __ (noun), and 
#___(adj) paper, members of Congress spent ___ (noun) in a special session Monday drawing ___ (adj) 
#pictures of their __(adj) Capitols, sources reported.

#The drawings—which variously featured huge ___ (noun) affixed to the Capitol dome, a moat 
#___ (verb) with crocodiles and __ (animal), and a ___ (adj) version of Sen. Marco Rubio (R-FL) that can ___ (verb) on 
#bills when the senator himself is ___ (ajd)—were reportedly part of an activity devised by congressional 
#____ (noun) to alleviate some of the stress caused by ___(ajd) bipartisan squabbling and to keep the lawmakers 
#___ (verb) until recess.


             
madLibDescriptions = ["noun"
                      , "noun"
                      , "adjective"
                      , "noun"
                      , "adjective"
                      , "adjective"
                      , "noun"
                      , "verb"
                      , "animal"
                      , "adjective"
                      , "verb"
                      , "adjective"
                      , "noun"
                      , "adjective"
                      , "verb"]              
userInput = [] 

def play():
  printNow("Welcome to our madlib game. Please follow the prompts to enter words that we will use for the story")
  printNow("")
  getWords()
  printNow(makeAdlib())
  
                      
def getWords():
   for descript in madLibDescriptions:
      printNow("Please enter a(n) " + descript + ": ")
      userInput.append( raw_input().lower() )
                      
def makeAdlib():
   index = 1
   finalString = ""
   for word in userInput:
      rawString.insert(index, word)
      index += 2
      
   for word in rawString:
      finalString += word
    
   return finalString

play()

