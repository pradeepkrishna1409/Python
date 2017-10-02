import json
class rect(object):
   def __init__(self,x=1,y=1,w=10,h=5):
      self.geom = {'x':x, 'y':y, 'width': w, 'height': h}

   def __repr__(self):
      return (json.dumps(self.geom))

def getKey(item):
   return item[0]

def intersection(r1,r2):
   # rect 1
   x11 = r1.geom['x']
   x12 = x11 +  r1.geom['width']
   y11 = r1.geom['y']
   y12 = y11 + r1.geom['height']

   # rect 2
   x21 = r2.geom['x']
   x22 = x21 +  r2.geom['width']
   y21 = r2.geom['y']
   y22 = y21 + r2.geom['height']

   # construct list of tuples
   x = [(x11,x12),(x21,x22)]
   y = [(y11,y12),(y21,y22)]

   # sort the list
   x = sorted(x, key=getKey)
   y = sorted(y, key=getKey)

   # get intersection
   xmin = x[0][0]
   xmax = x[1][1]

   if x[0][1] > x[1][0]:
      xmin = x[1][0]
      xmax = x[0][1]
   else:
      xmin = None
      xmax = None

   if y[0][1] > y[1][0]:
      ymin = y[1][0]
      ymax = y[0][1]
   else:
      ymin = None
      ymax = None

   return (xmin,xmax),(ymin,ymax)

if __name__=='__main__':
   # rect (x=1,y=1,w=10,h=5):

   r1 = rect(2,2,2,2)
   r2 = rect(1,1,2,2)
   #r2 = rect(0,0,1,1)
   #r2 = rect(3,3,2,2)
   #r2 = rect(5,5,1,1)
   print 'r1 = ', r1
   print 'r2 = ', r2

   x,y = intersection(r1,r2)
   if x[0] == None or x[1] == None or y[0] == None or y[1] == None:
      print 'No overlap'
   else:
      rOverlapped = rect(x[0],y[0],x[1]-x[0],y[1]-y[0])
      print 'rOverlapped = ', rOverlapped