# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------
# Lab 14, file IO test

# Written by: Matt Valancy (Crenshaw)

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Function header template   -----------------------------------
# ------------------------------------------------------------------------------------------------------------
# Function: What does it do
# Params: What does it accept
# Returns: What does it return


# Function: Green eggs total word count, unique word counts, most common word count
# Params: nothing
# Returns: nothing

def greenEggs():
   eggText = open("testfiles\eggs.txt").read()
   words = eggText.split()
   uniqueWords = []
   wordCounts = {}

   index = 0

   totalWords = len(words)
    
   for word in words:
      lword = word.lower()
      if lword not in uniqueWords:
         uniqueWords.append(lword)
         wordCounts[lword] = 1
      else:
         wordCounts[lword] += 1
       
   max = 0
   maxWord = ""
   for word in uniqueWords:
       if wordCounts[word] > max:
       	   max = wordCounts[word]
       	   maxWord = word
   
   print()
   print("Total words:" + str(totalWords))
   print()
   print("Word counts:")
   print (wordCounts)
   print()
   print ("Max word: " + maxWord + ":" + str(max) )


# Function: Search the otter news for some godo stuff
# Params: nothing
# Returns: nothing
def otterNews():
   newsText = open("testfiles\otternews.html").read() 
   totalLength = len(newsText)
   headingCount = newsText.count("<h3>")
   headings = []

   print(headingCount)   

   # get rid of extra junk
   startIndex = newsText.find("<h3>")
   endIndex = newsText.rfind("</h3>")
   newsText = newsText[startIndex:endIndex]

   
   
   
   index = 0
   for count in range(headingCount):
      start = newsText.find("<h3>", index) + 4
      end = newsText.find("</h3>", start)
      index = end
      headings.append(newsText[start:end])
   

   for text in headings:
      try: 
      	print(text)
      except:
      	print("string has error..")
         
    
greenEggs()
otterNews()