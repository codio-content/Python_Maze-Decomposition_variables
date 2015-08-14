
maze = False
player = False
width = 0
height = 0
numMonsters = 0
numOthers = 0
monsters = 0
walls = 0 
energies = 0

def createEmptyMaze(w, h):
  global width
  width = w
  global height
  height = h
  global maze
  maze = True

def addRandomMonsters(n):
  global monsters
  monsters = n
  
def addRandomWalls(n):
  global walls
  walls = n
  
def addRandomEnergies(n):
  global energies
  energies = n

def addPlayer():
  global player
  ppayer = True
  
  
try:
  execfile('/home/codio/workspace/public/py/py-5.py')
    
  if width == 10 and height == 8 and numMonsters == 2 and monsters == 2 and numOthers == 3 and  walls == 3 and energies == 3:
    print 'well done'
    exit(0)
except (IOError, SyntaxError) as e:
  print e
  pass
  
print 'Not quite right, try again!'
exit(1)
