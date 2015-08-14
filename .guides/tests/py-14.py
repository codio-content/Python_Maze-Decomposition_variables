
maze = False
message = ''

def createEmptyMaze():
  global maze
  maze = True

def showMessage(m):
  global message
  message = m
  
try:
  execfile('/home/codio/workspace/public/py/py-14.py')
    
  if maze == True and message == 'Mary had a little lamb':
    print 'well done'
    exit(0)
except (IOError, SyntaxError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
