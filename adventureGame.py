# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------
# The ultimate adventure game  
# Written by: CSIT group BitSoft

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Function header template   -----------------------------------
# ------------------------------------------------------------------------------------------------------------
# Function: What does it do
# Params: What does it accept
# Returns: What does it return

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Player variables  --------------------------------------------
# ------------------------------------------------------------------------------------------------------------

winner = False
hasSpaceSuit = False
isSlideDoorOpen = False
hasGun = False
lastRoom = 0

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Play game  ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Start the game here, run the game loop while room > 0 (you're alive and on the ship)
# Params: (none)
# Returns: (none)
def play():
  global hasSpaceSuit
  global isSlideDoorOpen
  global winner
  global hasGun
  hasSpaceSuit = False
  isSlideDoorOpen = False
  hasGun = False
  exiting = False
  winner = False
  firstRoom = True
  room = 1 # Begin game in room 1 (medical bay)
  
  printNow("\n *----  Welcome to Marooned in Space!  -----*")
  printNow(" |  You're in a large space station. A few hundred people used to live here, but they were attacked")
  printNow(" |  by an unknown threat. Everyone evacuated. You are still here because you were in the medical")
  printNow(" |  unit recovering from an explosion that heppened during routine maintenance. You were")
  printNow(" |  unconscious when the attack happened and missed the action. Explore the ship, stay alive, find")
  printNow(" |  your way back to earth...")
  printNow(" *")
  printNow("") # add some space
  displayHelp() 
  
  while room > 0:
    printNow("")
    if room == 1:
      room = roomOne(firstRoom)
      firstRoom = False
    elif room == 2:
      room = roomTwo() 
    elif room == 3:
      room = roomThree()
    elif room == 4:
      room = roomFour()
    elif room == 5:
      room = roomFive()
    elif room == 6:
      room = roomSix()
    lastRoom = room
  if winner:
    printNow(" Safe in the missile with your space suit you brace yourself for the engine to fire. It's only a matter of time before you are back")
    printNow(" on earth with your family again. Who knows what your next adventure will be...")
    printNow(" *")

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Room functions   ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #1 (A.K.A. "Medical Bay").
# Params:
#   firstRoom -> True if it is the first room entered (start of game), false otherwise.
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 1
#   Room name   -> "Medical Bay"
#   Exits       -> East (utility tunnel)               to room 2 ("Space Walk Utility Room")
#               -> South (airlock)                     to room 4 ("Transit Bay")
#               -> [hidden exit] North (sliding panel) to room 6 ("Drug Closet")
def roomOne(firstRoom):
  global lastRoom
  global isSlideDoorOpen
  
  if lastRoom != 1 or firstRoom:
    printNow(" -----  Medical Bay  -----")
    printNow(" You are standing in the medical bay. To the south is an airlock. To the east is the utility tunnel.")
    printNow(" To the north is a medical cabinet that looks like it has already been plundered for supplies.")
    printNow("")

  lastRoom = 1
  cmd = getDirection()
  
  if cmd == "search cabinet":
    printNow(" It looks like the cabinet might be able to slide if you pushed it.")
    printNow("")
    cmd = getDirection()
  if "cabinet" in cmd and ("slide" in cmd or "push" in cmd): 
    printNow(" You push the cabinet out of the way, opening a door to the north. It will spring shut if you walk")
    printNow(" away, so be careful.")
    printNow("")
    
    isSlideDoorOpen = True
    cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 1
  elif cmd == "east" or cmd == "e":
    return 2
  elif cmd == "south" or cmd == "s":
    return 4
  elif cmd == "north" or cmd == "n":
    if isSlideDoorOpen:
      printNow(" You sneak into the hidden medical closet.")
      return 6
    else:
      printNow(" You run into the medical cabinet and it shakes a bit, maybe you should search it more closely.")  
  displayInvalidDirection()
  return 1

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #2 (A.K.A. "Space Walk Utility Room").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 2
#   Room name   -> "Space Walk Utility Room"
#   Exits       -> West (utility tunnel)               to room 1 ("Medical Bay")
#               -> South (airlock)                     to room 3 ("Cafeteria")
#   * User can grab the space suit to win the game here (set hasSpaceSuit to True).
def roomTwo():
  global lastRoom
  global hasSpaceSuit
  
  if lastRoom != 2:
    printNow(" -----  Space Walk Utility Room  -----")
    printNow(" You are standing in the space walk utility room. To the north is the utility tunnel to the medical")
    printNow(" bay. To the south is an airlock.")
    printNow("")

  lastRoom = 2
  cmd = getDirection()
  
  if not hasSpaceSuit: 
    printNow(" There is a space suit here.")
    if "get" in cmd and "suit" in cmd: # Looking for something like "get space suit"
      hasSpaceSuit = True
      printNow(" You have picked up the space suit.")
      # Get a new command from the user if they got the space suit.
      cmd = getDirection() 
  if cmd == "north" or cmd == "n": 
     return 1
  elif cmd == "south" or cmd == "s":
     return 3
  elif isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 2
  displayInvalidDirection()
  return 2

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #3 (A.K.A. "Cafeteria").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 3
#   Room name   -> "Cafeteria"
#   Exits       -> North (airlock)                     to room 2 ("Space Walk Utility Room")
#               -> West (catwalk)                      to room 4 ("Transit Bay")
def roomThree():
  global lastRoom
  
  if lastRoom != 3:
    printNow(" -----  Cafeteria  -----")
    printNow(" You are standing in the cafeteria. To the West is a catwalk that looks like it could be sketchy. To")
    printNow(" the north is an airlock. In the corner of the room there is a shadow of what looks like a person. ")
    printNow("Possibly a survivor? ")
    printNow("")

  lastRoom = 3
  cmd = getDirection()
  
  #add something here for option of saying hello. Death if the user doesn't have the gun, and killing the alien if the user does. 
  
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 3
  if cmd == "north" or cmd == "n":
    return 2
  if cmd == "west" or cmd == "w":
    return 4
  displayInvalidDirection()
  return 3

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #4 (A.K.A. "Transit Bay").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 4
#   Room name   -> "Transit Bay"
#   Exits       -> East (catwalk)  to room 3 ("Cafeteria")
#               -> North (airlock) to room 1 ("Medical Bay")
#               -> West (ladder)   to room 5 ("Missile Room")
def roomFour():
  global lastRoom
  global hasGun
  
  if lastRoom != 4:
    printNow(" -----  Transit Bay  -----")
    printNow(" You are standing in the transit bay. To the east is a catwalk. To the north is an airlock. There")
    printNow(" is a ladder here as well. On the ground there is a gun that has been abandoned. ")
    printNow("")

  lastRoom = 4
  cmd = getDirection()
  
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 4
  elif cmd == "use ladder" or cmd == "go up" or "climb ladder":
    if hasSpaceSuit:
      printNow(" It is a bit awkward with the space suit, but you make your way up the ladder.")
    return 5
  elif cmd == "north" or cmd == "n":
    return 1 
  elif cmd == "east" or cmd == "e":
    return 3
  displayInvalidDirection()
  return 4

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #5 (A.K.A. "Missile Room").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 5
#   Room name   -> "Missile Room"
#   Exits       -> South (ladder) to room 4 ("Transit Bay")
def roomFive():
  global hasSpaceSuit
  global winner
  global lastRoom
  
  if lastRoom != 5:
    printNow(" -----  Missile Room  -----")
    printNow(" You are standing in the missile room. There is a big red button here and a ladder leading back")
    printNow(" down to the transit bay.")
    printNow("")

  lastRoom = 5
  cmd = getDirection()

  if "button" in cmd and "press" in cmd:
    if hasSpaceSuit:
      printNow(" You press the red button, and hop into the missile.")
      winner = True
      return -1
    else:
      printNow(" You can't press that button without a space suit on, you'll die.") # we should let them die...
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 5
  displayInvalidDirection()
  return 5

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #6 (A.K.A. "Medical Closet").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 6
#   Room name   -> "[hidden] Medical Closet"
#   Exits       -> South (sliding panel) to room 1 ("Medical Bay")
def roomSix():
  global lastRoom
  
  if lastRoom != 6:
    printNow(" -----  Medical Closet  -----")
    printNow(" You are standing in the medical supply closet. To the south is the medical bay.")
    printNow(" Most of the medicines look like they have been taken. In the corner, you see a large ")
    printNow(" slime covered blob rifling through a pile of empty bottles and boxes. The alien seems ")
    printNow(" occupied and has not noticed you entering the closet yet.")

  lastRoom = 6
  cmd = getDirection()
  
  if "Alien" in cmd or "attack" in cmd:
    printNow("The alien turns around suddenly. It lunges in your direction, covering you in a mucus like ")
    printNow("slime from head to toe. The world starts to spin and slowly you notice the tingling feeling ")
    printNow("as the slime begins to burn. The room begins to spin and then goes dark.")
    return -2
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 6
  elif cmd == "south" or cmd == "s":
    return 1
  displayInvalidDirection()
  return 6

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Helper functions   -------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Gets instructions from user.
# Params: (none)
# Returns: The user's instructions as raw text.
def getDirection():
  printNow("\n What would you like to do?")
  userDirection = raw_input(" >>> ").lower()
  printNow("")
  return userDirection

# Function: Prints a goodbye message if the user wishes to quit.
# Params:
#   command -> The command the user input.
# Returns: What does it return
#   True -> User wishes to quit.
#   False -> User doesn't with to quit.
def isQuit(command):
  if command == "quit":
    printNow(" Luckily, you hid a cyanide capsule in your pocket. You pull it out and bite down on it. Goodbye.")
    return True
  return False

# Function: Prints helpful instructions if the user requests help.
# Params:
#   command -> The command the user input.
# Returns:
#   True -> User requested help.
#   False -> User did not request help.
def isHelp(command):
  if command == "help":
    displayHelp()
    return True
  return False

# Function: Displays helpful instructions.
# Params: (none)
# Returns: (none)
def displayHelp():
  printNow("\n *-----  Directions  -----*")
  printNow(" |  Movement: north (n), south (s), east (e), west (w).")
  printNow(" |  Items: get, press. Ex. \"get space suit\", \"press button\"")
  printNow(" |  Quit: \"quit\"")
  printNow(" |  Help: \"help\"")
  printNow(" *")

# Function: Displays invalid direction notification.
# Params: (none)
# Returns: (none)
def displayInvalidDirection():
  printNow(" Whoops, looks like you can't go that way.")
