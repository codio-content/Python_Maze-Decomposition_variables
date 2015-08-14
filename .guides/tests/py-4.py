
num = 0
maze = False
player = False
monsters = 0
walls = 0 
energies = 0

def createEmptyMaze():
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
  execfile('/home/codio/workspace/public/py/py-4.py')
    
  if monsters == 3 and walls == 3 and energies == 3 and num == 3:
    print 'well done'
    exit(0)
except (IOError, SyntaxError) as e:
  print e
  pass
  
print 'Not quite right, try again!'
exit(1)
