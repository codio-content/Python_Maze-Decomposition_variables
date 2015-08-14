
maze = False

def createEmptyMaze(w, h):
  global maze
  
  if w == 10 and h == 14:
    maze = True

try:
  execfile('/home/codio/workspace/public/py/py-3.py')
  
  if maze == True:
    print 'well done'
    exit(0)
except (IOError, SyntaxError, NameError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
