# ----------------------------------------------  Program information    --------------------------------------

# Image manipulation functions 
# Written by: Matthew Valancy

# ---------------------------------------------- Function header template -------------------------------------

# Function: What does it do
# Params: What does it accept
# Returns: What does it return
  

# ----------------------------------------------      Library imports    --------------------------------------

import time # for measuring execution time during tests
import os

# ----------------------------------------------    Coloring Functions   --------------------------------------

# Function: No blue removes blue from a picture 
# Params: source picture
# Returns: picture without blue
def noBlue(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    setBlue(p,0)
  return retPic


# Function: half red reduces the red in a picture by half
# Params: source picture
# Returns: picture with half as much red
def halfRed(sourcePic):  
  return lessRed(sourcePic, 0.50)


# Function: less red reduces the red in a picure by x%, but could actually increase red if given 110%...
# Params: source picture, precentage in whole number form (100 = 100%, etc)
# Returns: picture with less red
def lessRed(sourcePic, percent):
  retPic = duplicatePicture(sourcePic)
  percent /= 100.0
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percent)
  return retPic

  
# Function: increases red in a photo by adding 100 to the percent but doing the same thing as lessRed
# Params: source picture, percentage in whole number form (100 = 100%, etc)
# Returns:  picture with more red
def moreRed(sourcePic, percent):
  retPic = duplicatePicture(sourcePic)
  percent /= 100.0
  percent += 1.0
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percent)
  return retPic


# Function: reduce green to 30% and make everything pink inversely porportional to it's original pinkness
# Params: source pic
# Returns: rose colorized picture
def roseColoredGlasses(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    setGreen(p, g * 0.3)
    setRed(p, 255 - r)
    setBlue(p, 255 - b)
  return retPic


# Function: makes a color lighter
# Params: multiplies color by 1.5
# Returns:  new, brighter color
def makeLighter(oldColor):
  return oldColor * 1.5
  

# Function: Lighten a photo by 25% 
# Params: input photo to lighten
# Returns:  photo that is lighter than original
#increase image brightness by a fixed 25% 
def lightenUp(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    setRed(p, r * 1.25)
    setBlue(p, b * 1.25)
    setGreen(p, g * 1.25)
  return retPic


# Function: makes a photo it's negative 
# Params: source picture to invert
# Returns:  negative photo
#invert image
def makeNegative(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    setRed(p, 255 - r)
    setBlue(p, 255 - b)
    setGreen(p, 255 - g)
  return retPic
 

# Function: convert to grayscale by averaging all pixels (primitive B&W)
# Params: source picture to convert
# Returns: black and white photo
def BnW(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    average = r + b + g
    average /= 3
    setRed(p, average)
    setBlue(p, average)
    setGreen(p, average)
  return retPic


# Function:  better black and white photo
# Params:  source picture to convert
# Returns:  black and white photo
def betterBnW(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    average = (r * 0.299) + (b * 0.114) + (g * 0.587)
    setRed(p, average)
    setBlue(p, average)
    setGreen(p, average)
  return retPic


# Function: Sepia colorize
# Params: source image
# Returns: Sepia picture
def sepia(sourcePic):
  retPic = duplicatePicture(sourcePic)
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    if r < 63:
      r  *= 1.1
      b *= 0.9
    elif r < 192:
      r *= 1.15
      b *= 0.85
    else:
      r *= 1.08
      b *= 0.93
      if r > 255:
        r = 255
    setRed(p, r)
    setBlue(p, b)
  return retPic


# Function: Sepia colorize
# Params: source image
# Returns: Sepia picture
def artify(sourcePic):
  retPic = duplicatePicture(sourcePic)
  
  pixels = getPixels(retPic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    for color in [r, b, g]:
      if color < 64:
         color = 31
      elif color < 128:
        color = 95
      elif color < 192:
        color = 159
      else:
        color = 223        
    setRed(p, r)
    setBlue(p, b)
    setGreen(p, g)
    
  return retPic


# Function: Horizontal image mirroring
# Params: 1) an image, 2) bool value for True mirrors left to right, False mirrors right to left
# Returns: mirrored image
def mirrorHorizontal(sourcePic, leftRight):
  width = getWidth(sourcePic)
  height = getHeight(sourcePic)
  retPic = duplicatePicture(sourcePic)
  
  xEnd = width / 2   
    
  # mirror left to right side of image
  if leftRight == True:
    for y in range(0, height):
      for x in range(0, xEnd):
        sourcePixel = getPixel(sourcePic, x, y)
        destPixel = getPixel(retPic, width - x - 1, y)
        sourceColor = getColor(sourcePixel)
        setColor(destPixel, sourceColor)
  #mirror right to left side of image
  else:
    for y in range(0, height):
      for x in range(0, xEnd):
        sourcePixel = getPixel(sourcePic, width - x - 1, y)
        destPixel = getPixel(retPic, x, y)
        sourceColor = getColor(sourcePixel)
        setColor(destPixel, sourceColor)
   
  return retPic
  

# Function: Vertical image mirroring
# Params: 1) an image, 2) bool value for True mirrors top to bottom, False mirrors bottom to top
# Returns: mirrored image
def mirrorVertical(sourcePic, topBottom):
  width = getWidth(sourcePic)
  height = getHeight(sourcePic)
  retPic = duplicatePicture(sourcePic)
  
  yEnd = height / 2   
    
  # mirror top to bottom side of image
  if topBottom == True:
    for x in range(0, width):
      for y in range(0, yEnd):
        sourcePixel = getPixel(sourcePic, x, y)
        destPixel = getPixel(retPic, x, height - y - 1)
        sourceColor = getColor(sourcePixel)
        setColor(destPixel, sourceColor)
  #mirror bottom to top side of image
  else:
    for x in range(0, width):
      for y in range(0, yEnd):
        sourcePixel = getPixel(sourcePic, x, height - y - 1)
        destPixel = getPixel(retPic, x, y)
        sourceColor = getColor(sourcePixel)
        setColor(destPixel, sourceColor)
  
  return retPic


# Function: Quadrant mirroring (1 top left, 2 top right, 3 bottom left, 4 bottom right) 
# Params: picture to use, quadrant to select (1,2,3,4)
# Returns: mirrored picture
def quadMirror(sourcePic, quadrant):
  retPic = duplicatePicture(sourcePic)
  #Mirror top left corner to all other corners of the picture
  if quadrant == 1:
    retPic = mirrorHorizontal(retPic, True)
    retPic = mirrorVertical(retPic, True)
  
  #Mirror top right corner to all other corners of the picture
  elif quadrant == 2:
    retPic = mirrorHorizontal(retPic, False)
    retPic = mirrorVertical(retPic, True)
  
  #Mirror bottom left corner to all other corners of the picture
  elif quadrant == 3:
    retPic = mirrorVertical(retPic, False)
    retPic = mirrorHorizontal(retPic, True)
  
  #Mirror bottom right corner to all other corners of the picture
  else:
    retPic = mirrorVertical(retPic, False)
    retPic = mirrorHorizontal(retPic, False)
   
  return retPic
  
  
# Function: Rotate image 90 degrees CCW or CW
# Params: picture to rotate, [CCW == True] rotates CCW,  [CCW == Talse] rorates CW
# Returns: rotated picture
def rotatePic(sourcePic, CCW):
  sourceHeight = sourcePic.getHeight()
  sourceWidth = sourcePic.getWidth()
  retPic = makeEmptyPicture (sourceHeight, sourceWidth)

  #Work from top to bottom of source picture moving one row at a time left to right
  #Copy to source picture working from bottom left corner up one column at a time left to right
  if CCW == True:
    for sourceY in range(0, sourceHeight):
      for sourceX in range(0, sourceWidth):
        sourcePixel = getPixel(sourcePic, sourceX, sourceY)
        destPixel   = getPixel(retPic, sourceY, sourceWidth - sourceX - 1)
        setColor(destPixel, getColor(sourcePixel))       
        
  #Work from top to bottom of source picture moving one row at a time left to right
  #Copy to source picture working from bottom right corner up one column at a time right to left
  else:
    for sourceY in range(0, sourceHeight):
      for sourceX in range(0, sourceWidth):
        sourcePixel = getPixel(sourcePic, sourceX, sourceY)
        destPixel   = getPixel(retPic, sourceHeight - sourceY - 1, sourceX)
        setColor(destPixel, getColor(sourcePixel))
        
  return retPic          
  

# Function: Shrink an image by 50%
# Params: Picture to scale
# Returns: Resized picture
def shrink(sourcePic):
   sourceHeight = sourcePic.getHeight()
   sourceWidth = sourcePic.getWidth()
   retPic = makeEmptyPicture(sourceWidth/2, sourceHeight/2)
   destX = 0
   destY = 0
   destWidth = retPic.getWidth()
   destHeight = retPic.getHeight()
   
   for sourceY in range(0, sourceHeight, 2):
     destX = 0
     for sourceX in range(0, sourceWidth, 2):
       if(destX < destWidth) and (destY < destHeight):   
         sourcePixel = getPixel(sourcePic, sourceX, sourceY)
         destPixel   = getPixel(retPic, destX , destY)
         setColor(destPixel, getColor(sourcePixel))
       destX += 1     
     destY += 1
     
   return retPic


# Function: Copy source image to target image
# Params: source image, target image, target x for 0, target y for 0    
# Returns: Resized picture
def pyCopy(source, target, targetX, targetY):
  targetWidth = target.getWidth()
  targetHeight = target.getHeight()

  for y in range(0, source.getHeight()):
    if y + targetY < targetHeight:
      for x in range(0, source.getWidth()):
        if x + targetX < targetWidth:
          sourcePixel = getPixel(source, x, y)
          sourceColor = getColor(sourcePixel)
          destPixel = getPixel(target, x + targetX, y + targetY)
          destPixel.setColor(sourceColor)


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


# Function: Green screen foreground onto background
# Params: background picture, foreground picture
# Returns: combined photo
def chromaKey(foreground, background):
  greenScreen = [16, 223, 13] # R G B values for green screen
  colorPrecision = 150 # how close the colors has to be to remove the alpha
  retPic = duplicatePicture(background)
  pyCopyA(foreground, retPic, 0, 0, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)  
  return retPic


# ---------------------------------------------- Test code section --------------------------------------


# Function: Make a collage with dragons, fire balls, and a drone
# Params: none, you can't negotiate with dragons
# Returns: final image
def makeCollage():
  finalImage = makeEmptyPicture(1256, 712)
  greenScreen = [16, 223, 13] # R G B values for green screen
  colorPrecision = 150 # how close the colors has to be to remove the alpha
  
  # Load up all images before we start the party
  background = makePicture("C:\Matt\CSUMB\Project1\collage\\background.jpg")
  title = makePicture("C:\Matt\CSUMB\Project1\collage\\title.jpg")
  moon = makePicture("C:\Matt\CSUMB\Project1\collage\\moon.jpg")
  dinosaur = makePicture("C:\Matt\CSUMB\Project1\collage\\dinosaur.jpg")
  fireballA = makePicture("C:\Matt\CSUMB\Project1\collage\\fireball.jpg")
  treeA = makePicture("C:\Matt\CSUMB\Project1\collage\\tree1.jpg")
  treeB = makePicture("C:\Matt\CSUMB\Project1\collage\\tree2.jpg")
  treeC = makePicture("C:\Matt\CSUMB\Project1\collage\\tree3.jpg")
  
  # Do secondary processing to images to generate additional assets
  smallDinoA = shrink(dinosaur)
  smallDinoB = rotatePic(smallDinoA, True)
  smallDinoC = rotatePic(smallDinoB, True)
  fireballB = rotatePic(fireballA, True)
  fireballB = rotatePic(fireballB, True)
  treeC = shrink(treeC)
  
  # Paint the scene
  pyCopy(background, finalImage, 0, 0)
  pyCopyA(title, finalImage, 350, 50, greenScreen[0], greenScreen[1], greenScreen[2], 200)  
  pyCopyA(moon, finalImage, -20, -20, greenScreen[0], greenScreen[1], greenScreen[2], 200)  
  pyCopyA(treeB, finalImage, 0, 0, greenScreen[0], greenScreen[1], greenScreen[2], 200)  
  pyCopyA(treeC, finalImage, 0, 450, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)  
  pyCopyA(treeC, finalImage, 900, 450, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)  
  pyCopyA(treeA, finalImage, 900, 400, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)  
  # Warning, impending dinosaur attack
  pyCopyA(fireballA, finalImage, 800, 50, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)
  pyCopyA(fireballB, finalImage, 300, 200, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)
  pyCopyA(smallDinoA, finalImage, -30, 200, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)
  pyCopyA(smallDinoB, finalImage, 600, 400, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)
  pyCopyA(smallDinoC, finalImage, 900, -20, greenScreen[0], greenScreen[1], greenScreen[2], colorPrecision)
  
  return finalImage
  

  
  
#---------------- Green screen test
#foreground = makePicture("C:\Matt\CSUMB\Project1\collage\\scifiShip.jpg")
#background  = makePicture("C:\Matt\CSUMB\Project1\collage\\grassLand.jpg")
#finalImage = chromaKey(foreground, background)
#show(finalImage)
#----------------

#frame.visible = True

#startTime = time.time()

#showImage(makeCollage())
#sourcePic = makePicture(pickAFile())
#targetPic = makeEmptyPicture(sourcePic.getWidth() * 2, sourcePic.getHeight() * 2)
#pyCopy(sourcePic, targetPic, 500, 20)
#show(targetPic)
#print "processing time:" + str(time.time() - startTime)
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
print(dname)
os.chdir(dname)
artPic = makePicture("\images\\backgroundTest.jpg")
artPic = sepia(artPic)
#artPic = betterBnW(artPic)
show(artPic)



