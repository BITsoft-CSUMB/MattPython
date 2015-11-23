# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Instagram style filters 
# Filter 1: Scuba themed
# Filter 2: Fungal themed
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
   print "mediaPath = " + setMediaPath("C:\\Matt\\BitsoftGit-MattV\\testimages\\")
except ValueError: 
   print "mediaPath:" + setMediaPath()

oceanLightPic = "geometric.jpg"

# ------------------------------------------------------------------------------------------------------------  
# ----------------------------------------------      Library imports    -------------------------------------
# ------------------------------------------------------------------------------------------------------------
import media
#from imagemanip import *
#import mattlib.imagemanip
#!!! JES seems jacked so I am giving up on custom libraries


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------      Shared Functions   -------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Scale Matching so that we can dynamically apply textures like bubbles or light effects to scenes without massive cropping
# Params: fixedPic is the picture whose dimensions we don't want to adjust, rescalePic is the one we want to approximately match and trim
# Returns: Resized version of rescalePic which is probably going to be slightly bigger than fixedPic depending on the difference between their size ratio
def scaleMatch(fixedPic, rescalePic):
   fWidth  = float(fixedPic.getWidth())
   fHeight = float(fixedPic.getHeight())
   rWidth  = float(rescalePic.getWidth())
   rHeight = float(rescalePic.getHeight())
   #retPic = makeEmptyPicture(int(fWidth), int(fHeight))
  
   scale = 0
   # meat and potatoes, figure out how we want to scale the picture, will scaling the height leave the width too small etc
   # first compare the height, is the picture to resize bigger or smaller than the fixed pic?
   if(rHeight < fHeight): 
      scale = (rHeight / fHeight) + 1.0
      showInformation("1: " + str(scale))
      if( (rWidth * scale) < fWidth):  #what happens to the width if you apply scale, will it make it too small?
         scale = (rWidth / fWidth) + 1.0
         showInformation("2: " + str(scale))
   else: 
      scale = 1.0/(rHeight/fHeight) 
      showInformation("3: " + str(scale))
      if( rWidth * scale < fWidth):
         scale = fWidth / rWidth + 1.0
         showInformation("4: " + str(scale))
         

   # convert to regular % like 90% 110% etc
   scale = (scale * 100.0) # oversize by 10% to account for rounding errors
  
   # apply shrink ray in 3...2...1..
   retPic = resize(rescalePic, scale)
   retPicWidth = retPic.getWidth()

   # now trim the fat off the sides of the picture
   xTrim = int((retPicWidth - fWidth) / 2.0)   
   retPic = crop (retPic, xTrim, retPicWidth - xTrim, 0, int(fHeight))
   
   return retPic

def crop(sourcePic, xStart, xEnd, yStart, yEnd):
   retPicWidth = xEnd - xStart
   retPicHeight = yEnd - yStart
   retPic = makeEmptyPicture(retPicWidth, retPicHeight)
  
   targetX = 0
   targetY = 0
   
   for sourceY in range(yStart, yEnd):
      targetX = 0
      for sourceX in range(xStart, xEnd):
         if(targetX < retPicWidth and targetY < retPicHeight):
            sourcePixel = getPixel(sourcePic, sourceX, sourceY)
            targetPixel = getPixel(retPic, targetX, targetY)
            setColor(targetPixel, getColor(sourcePixel))
         targetX += 1
      targetY += 1
   
   return retPic


# Function: Scale an image by X% (50%, 110%, etc)
# Params: Picture to scale
# Returns: Resized picture
def resize(sourcePic, percent):
   if(percent == 100): 
      return duplicatePicture(sourcePic)
   if(percent == 0):
      return makeEmptyPicture(1,1)

   sourceHeight = sourcePic.getHeight()
   sourceWidth = sourcePic.getWidth()
   
   scaleFactor = percent / 100.0  
   print scaleFactor

   retPic = makeEmptyPicture( int(sourceWidth * scaleFactor), int(sourceHeight * scaleFactor) )
   
   destWidth = retPic.getWidth()
   destHeight = retPic.getHeight()
   
   sourceX = 0
   sourceY = 0
   destX = 0
   destY = 0
   
   if(scaleFactor < 1): #Shrink
      
      skip = int(round(1/scaleFactor)) # skip count go by 1, 2, 3, etc.
      
      showInformation(str(skip))
      for sourceY in range(0, sourceHeight, skip):
         destX = 0
         for sourceX in range(0, sourceWidth, skip):
            if(destX < destWidth) and (destY < destHeight):   
               sourcePixel = getPixel(sourcePic, sourceX, sourceY)
               destPixel   = getPixel(retPic, destX , destY)
               setColor(destPixel, getColor(sourcePixel))
            destX += 1     
         destY += 1
         
        
   else: #Enlarge is the opposite of shrink, we duplicate pixels from source to destination and only increment soureX or source Y every destX%skip or destY%skip
      heightRatio = destHeight / sourceHeight
      widthRatio  = destWidth  / sourceWidth
      
      for sourceY in range (0, sourceHeight):
         for sourceX in range (0, sourceWidth):
            sourcePixel = getPixel(sourcePic, sourceX, sourceY)
            sourceColor = getColor(sourcePixel)
            for destX in range(0, widthRatio):
               for destY in range(0, heightRatio):
                  destPixel = getPixel(retPic, widthRatio * sourceX + destX, heightRatio * sourceY + destY)
                  setColor(destPixel, sourceColor)
            
     
   return retPic


# Function: Blend a foreground and background based on transparency percent applied to foreground
# Params: Background image, foreground image, percent 0-100 to blend
# Returns: Resized version of rescalePic which is probably going to be slightly bigger than fixedPic depending on the difference between their size ratio
def blend(background, foreground, percent):
  retPic = duplicatePicture(background)

  if(percent == 0):
    return background
  if(percent == 100):
    return foreground
  
  fgPercent = percent / 100.0
  bgPercent = (100 - percent) / 100.0

  setColorWrapAround(false) # dont trip about color values > 255 or < 0

  bgWidth = background.getWidth()
  bgHeight = background.getHeight()
  fgWidth = foreground.getWidth()
  fgHeight = foreground.getHeight()

  for y in range (0, bgHeight): #top to bottom left to right, blend some pixels based on % of foreground
    if(y < fgHeight):
      for x in range (0, bgWidth):
        if(x < fgWidth):
          bgPixel = getPixel(retPic, x, y)
          fgPixel = getPixel(foreground, x, y)
          
          bgPixelG = getGreen(bgPixel)
          bgPixelR = getRed(bgPixel)
          bgPixelB = getBlue(bgPixel)
          
          fgPixelG = getGreen(fgPixel)
          fgPixelR = getRed(fgPixel)
          fgPixelB = getBlue(fgPixel)
          
          bgPixelG = (fgPixelG * fgPercent) + (bgPixelG * bgPercent)
          bgPixelR = (fgPixelR * fgPercent) + (bgPixelR * bgPercent)
          bgPixelB = (fgPixelB * fgPercent) + (bgPixelB * bgPercent)

          setColor(bgPixel, makeColor(bgPixelR, bgPixelG, bgPixelR) )
  return retPic


# Function: Blend a foreground and background based on transparency percent applied to foreground while resizing the foreground to closely match the background
# Params: Background image, foreground image, percent 0-100 to blend
# Returns: Resized version of rescalePic which is probably going to be slightly bigger than fixedPic depending on the difference between their size ratio
def smartBlend(background, foreground, percent):
  scaledForeground = scaleMatch(background, foreground)
  return blend(background, scaledForeground, percent)


# Function: python copy with alpha, copy source image to target image and remove transparent pixels
# Params: source image, target image, target x for 0, target y for 0 
# Returns: Resized picture
def pyCopyA(source, target, targetX, targetY, alphaR, alphaG, alphaB, precision):
  targetWidth = target.getWidth()
  targetHeight = target.getHeight()

  for y in range( 0, source.getHeight() ): # work from top to bottom
    if (y + targetY < targetHeight) and (y + targetY > 0): #Y range check so we can go crazy and not worry
      for x in range( 0, source.getWidth() ):
        if (x + targetX < targetWidth) and (x + targetX > 0): #X range check so we can go crazy and not worry
          sourcePixel = getPixel(source, x, y)
          sourceColor = getColor(sourcePixel)
          if ( abs(sourceColor.getRed() - alphaR) + abs(sourceColor.getBlue() - alphaB) + abs(sourceColor.getGreen() - alphaG) ) > precision: 
            destPixel = getPixel(target, x + targetX, y + targetY)
            destPixel.setColor(sourceColor)          


# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Filter 1 - under the C...sumb (scuba) -----------------------
# ------------------------------------------------------------------------------------------------------------

# Function: COLOR SHIFT, Remove colors according to what travels best underwater
# Params: Source picture
# Returns: Picture with color adjustment
# Reference: for absorption underwater see http://www.scuba-tutor.com/dive-physics/water-density/color-absorption.php
def oceanColor(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
     setRed(p, getRed(p) * 0.3)
     setGreen(p, getGreen(p) * 0.6)
  return retPic

# Function: IMAGE TEXTURIZE, Applies lighting and water artificts like bubbles and specks
# Params: Source picture
# Returns: Picture with light and particle effectsmakeEmptyPicture(
def oceanLight(sourcePic):
  retPic = duplicatePicture(sourcePic)
  lightPic = makeImage( getMediaPath(oceanLightPic) )

  
  sWidth = sourcePic.getWidth()
  sHeight = sourcePic.getHeight()
  lWidth = lightPic.getWidth()
  lHeight = lightPic.getHeight()

  
  

# Function: Add kelp to an image
# Params: Source picture
# Returns: Picture with kelp added
def addKelp(sourcePic):
   test = 0


# Function: Add fish
# Params: Source picture
# Returns:Picture with fish added
def addFish(sourcePic):
   test = 0


# Function: Applies scuba themed filter to source picture
# Params: Source picture
# Returns: Scuba themed pic
def scubaFilter(sourcePic):
   retpic = oceanColor(sourcePic)
   retPic = oceanLight(sourcePic)
   retPic = addKelp(sourcePic)
   retPic = addFish(sourcePic)
   return retPic

# ------------------------------------------------------------------------------------------------------------
# -------------------------------------Filter 2 - microrizial invasion(fungus) -------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Remove colors according to what travels best underwater
# Params: Source picture
# Returns: Picture with color adjustment
# Reference for absorption underwater: http://www.scuba-tutor.com/dive-physics/water-density/color-absorption.php
def fungalColor(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
     setRed(p, getRed(p) * 0.3)
     setGreen(p, getGreen(p) * 0.6)
  return retPic

# Function: Applies lighting effects with a fungal theme
# Params: Source picture
# Returns: Picture with light and particle effects
def fungalLght(sourcePic):
  retPic = duplicatePicture(sourcePic)

  
# Function: Applies lighting and 
# Params: Source picture
# Returns: Picture with light and particle effects
def addMushrooms(sourcePic):
   retPic = duplicatePicture(sourcePic)
  

# Function: Applies fungal themed filter to source picture
# Params: Source picture
# Returns: Fungal themed pic
def fungalFilter(sourcePic):
  retpic = fungalColor(sourcePic)
  retPic = fungalLight(sourcePic)
  retPic = addMushrooms(sourcePic)
  return retPic

# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------      Filter Tests      --------------------------------------
# ------------------------------------------------------------------------------------------------------------
def scubaTest():
   testPic = makePicture(getMediaPath("mrrogers.jpg"))
   #testPic = oceanColor(testPic)
   lightPic = makePicture(getMediaPath(oceanLightPic))
   show(smartBlend(testPic, lightPic, 40))
   
   #show(testPic)
   #show(lightPic)
   #show(scaleMatch(testPic, lightPic))
def fungusTest():
   test = 0


#try:
#pic = duplicatePicture(pic)
#pic = halfRed(pic) 
#except NameError:
#print "can't shrink"


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------   Code that runs on start of script      --------------------
# ------------------------------------------------------------------------------------------------------------
print "test"
scubaTest()
fungusTest()


