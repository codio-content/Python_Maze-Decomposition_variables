
maze = False

def createEmptyMaze(w, h):
  global maze
  
  if w == 8 and h == 6:
    maze = True

try:
  execfile('/home/codio/workspace/public/py/py-1a.py')
  
  if maze == True:
    print 'well done'
    exit(0)
except (IOError, SyntaxError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
