# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Sound manipulation functions
# Written by: Matthew Valancy


# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Function header template ------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: What does it do
# Params: What does it accept
# Returns: What does it return


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------      File Setup          ------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Change the static folder names, or use the dialogs to first set your library path
# followed by your picture path.

#try: 
#   print "libpath = " + setLibPath("C:\\Matt\\BitsoftGit-MattV\\")
#except ValueError:
#   print "libPath:" + setLibPath()
 
try: 
   print "mediaPath = " + setMediaPath("C:\\Matt\\BitsoftGit-MattV\\testsounds\\")
except ValueError: 
   print "mediaPath:" + setMediaPath()


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------      Lab 8               ------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Increase volume of a sound file by factor of 2
# Params: sound file 
# Returns: nothing, it modifies the sound given in the parameter
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)


# Function: Decrease volume of a sound file by factor of 2
# Params: sound file 
# Returns: nothing, it modifies the sound given in the parameter
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / 2)

        
# Function: Increase volume of a sound file by factor of 2
# Params: sound file, percent increase/decrease(150%, 100%, 50%, etc)
# Returns: nothing, it modifies the sound given in the parameter
def changeVolume(sound, percent):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      factor = percent / 100.0
      setSampleValue(sample, value * factor)


# Function: Find the maximum amplitude in the sound file
# Params: Sound file to search
# Returns: Maximum amplitude
def maxSample(sound):
   samples = getSamples(sound)
   max = 0
   current = 0
   
   for i in range(0, len(samples)):
      current = getSampleValue(samples[i])
      if(current > max):
         max = current
   return max


# Function: Increase volume of a sound file to the max
# Params: sound file
# Returns: modified sound (but it also modifies the original)
def maxVolume(sound):
   samples = getSamples(sound)
   max = maxSample(sound)
   soundFactor = 32767 / max
   
   for i in range(0, len(samples)):
      current = getSampleValue(samples[i])
      setSampleValue(samples[i], current * soundFactor)
   return sound

      
# Function: GoToEleven turns the nice sine wave into a square wave with maximum and minimum amplitude but nothing inbetween so it sounds bad
# Params: sound file
# Returns: modified sound (but it also modifies the original)
def goToEleven(sound):
   samples = getSamples(sound)
   
   for i in range(0, len(samples)):
      current = getSampleValue(samples[i])
      if(current > 0): 
         setSampleValue(samples[i], 32767)
      else:
         setSampleValue(samples[i], -32767)
   return sound
  
sounds = [makeSound(getMediaPath("shirley.wav")), makeSound(getMediaPath("bueller.wav")), makeSound(getMediaPath("score.wav"))]
shirleySound = makeSound(getMediaPath("shirley.wav"))
samples = getSamples(shirleySound)
#play(shirleySound)
print getSampleValueAt(shirleySound, 10000)

buellerSound = makeSound(getMediaPath("bueller.wav"))
changeVolume(sounds[1], 150)
#play(sounds[1])
#showInformation("max: " + str(maxSample(sounds[1])))
#changeVolume(sounds[1], 20)
goToEleven(sounds[1])
play(sounds[1])
play(maxVolume(sounds[1]))