# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
import math

transx=1
transy=1
transz=1
rotateangle=0
inside=0
backout=0
carx=0
currenttire=0
tirespin=0
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Line3D():

    def __init__(self, start, end):
        self.start = start
        self.end = end

def loadOBJ(filename):

    vertices = []
    indices = []
    lines = []

    f = open(filename, "r")
    for line in f:
        t = str.split(line)
        if not t:
            continue
        if t[0] == "v":
            vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))

        if t[0] == "f":
            for i in range(1,len(t) - 1):
                index1 = int(str.split(t[i],"/")[0])
                index2 = int(str.split(t[i+1],"/")[0])
                indices.append((index1,index2))

    f.close()

    #Add faces as lines
    for index_pair in indices:
        index1 = index_pair[0]
        index2 = index_pair[1]
        lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))

    #Find duplicates
    duplicates = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]

            # Case 1 -> Starts match
            if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
                if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
                    duplicates.append(j)
            # Case 2 -> Start matches end
            if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
                if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
                    duplicates.append(j)

    duplicates = list(set(duplicates))
    duplicates.sort()
    duplicates = duplicates[::-1]

    #Remove duplicates
    for j in range(len(duplicates)):
        del lines[duplicates[j]]

    return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))

    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))

    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))

    return tire


def drawMyCar(s):

  mylist=[]
  global transz
  global transx
  global transy
  global rotateangle
  global carx
  for u in range(2):
    x=0
    y=0
    z=0
    if u==0:
        x=s.start.x
        y=s.start.y
        z=s.start.z
    if u==1:
        x=s.end.x
        y=s.end.y
        z=s.end.z
    startpoint=np.matrix([[x, y, z, 1.0]], dtype=np.float64).T  #this changes the zoom
    #rotateangle=math.pi/2.0
    #print rotateangle
    rotatematrix=np.matrix([[math.cos(0), 0.0, -1.0*math.sin(0), 0.0],
    [0.0,1.0, 0.0, 0.0],
    [math.sin(0), 0.0, math.cos(0), 0.0],
    [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float64)
    transMatrix=np.matrix([[1, 0.0, 0, transx+carx],
    [0.0,1,0.0,transy],
    [0.0,0.0,1,transz],
    [0.0,0.0,0.0,1]],dtype=np.float64)
    #print startpoint,"startpoint", startpoint.shape
    #print rotatematrix, "rotatematrix", rotatematrix.shape
    #print transMatrix, " transmatrix", transMatrix.shape
    pworld=transMatrix*rotatematrix*startpoint
    #print "this my pworld ", pworld
    cameraposition=np.matrix([[1,0.0,0,-3],[0,1,0,-1], [0,0,1,40],[0,0,0,1]], dtype=np.float64)
    cameraangle=math.radians(rotateangle)
    rotatecamera=np.asarray([[math.cos(cameraangle), 0.0, -1.0*math.sin(cameraangle),0],
    [0.0, 1.0, 0.0, 0.0],
    [math.sin(cameraangle), 0.0, math.cos(cameraangle), 0.0],
    [0.0,0.0,0.0,1.0]],dtype=np.float64)


    pcam=rotatecamera*cameraposition*pworld
    #print "this is my pcam" ,pcam
    fov=pi/3
    zoomy=1/math.tan(fov/2)
    zoommatrix=np.matrix([[zoomy, 0, 0, 0],
[0, zoomy, 0, 0],
[0,0,1.02, -20.20],
[0,0,1,0]
    ])
    pclip=zoommatrix*pcam
    #print "my pclip ",pclip
    temp=np.where(pclip<pclip[3])
    temp=np.where(temp>pclip[3])
    temp=np.asarray(temp)
    if temp.size !=0:   #INVALID
        dude=[]
        dude.append([s.start.x, s.start.y, s.start.z])
        dude.append([s.end.x, s.end.y, s.end.z])
        #print "i don't draw it"
        return False
    pcanon=pclip/pclip[3]
    #print pcanon
    #print pcanon[0][0]
    #print pcanon[1][0]
    #print pcanon[3][0]
    dropz=np.matrix([[pcanon.item(0)],[pcanon.item(1)],[pcanon.item(3)]])
    #print dropz
    canonmatrix=np.matrix([[500/2.0, 0, 500/2],
    [0, -500/2, 500/2],
    [0,0,1]
    ])
    pscreen=canonmatrix*dropz
    #print pscreen
    if u==0:
        mylist.append([pscreen.item(0),pscreen.item(1),pscreen.item(2)])
    if u==1:
        mylist.append([pscreen.item(0),pscreen.item(1),pscreen.item(2)])

  #print "i return ", mylist
  return mylist

def drawMyWheels(s):
  mylist=[]
  global transz
  global transx
  global transy
  global rotateangle
  global carx
  global currenttire
  global tirespin
  xdisplacement=0
  zdisplacement=0
  if currenttire==0:
      tirespin-=0.1
      xdisplacement=-3
      zdisplacement=2
  if currenttire==1:
      xdisplacement=3
      zdisplacement=2
  if currenttire==2:
     xdisplacement=-3
     zdisplacement=-2
  if currenttire==3:
    xdisplacement=3
    zdisplacement=-2
  for u in range(2):
    x=0
    y=0
    z=0
    if u==0:
        x=s.start.x
        y=s.start.y
        z=s.start.z
    if u==1:
        x=s.end.x
        y=s.end.y
        z=s.end.z
    startpoint=np.matrix([[x, y, z, 1.0]], dtype=np.float64).T  #this changes the zoom
    #rotateangle=math.pi/2.0
    #print rotateangle
    rotatematrix=np.matrix([[math.cos(math.radians(tirespin)),-1*math.sin(math.radians(tirespin)),0.0,0.0],
    [math.sin(math.radians(tirespin)),math.cos(math.radians(tirespin)), 0.0, 0.0],
    [0.0,0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float64)
    transMatrix=np.matrix([[1, 0.0, 0, transx+carx+xdisplacement],
    [0.0,1,0.0,transy],
    [0.0,0.0,1,transz+zdisplacement],
    [0.0,0.0,0.0,1]],dtype=np.float64)
    #print startpoint,"startpoint", startpoint.shape
    #print rotatematrix, "rotatematrix", rotatematrix.shape
    #print transMatrix, " transmatrix", transMatrix.shape
    pworld=transMatrix*rotatematrix*startpoint
    #print "this my pworld ", pworld
    cameraposition=np.matrix([[1,0.0,0,-3],[0,1,0,-1], [0,0,1,40],[0,0,0,1]], dtype=np.float64)
    cameraangle=math.radians(rotateangle)
    rotatecamera=np.asarray([[math.cos(cameraangle), 0.0, -1.0*math.sin(cameraangle),0],
    [0.0, 1.0, 0.0, 0.0],
    [math.sin(cameraangle), 0.0, math.cos(cameraangle), 0.0],
    [0.0,0.0,0.0,1.0]],dtype=np.float64)


    pcam=rotatecamera*cameraposition*pworld
    #print "this is my pcam" ,pcam
    fov=pi/3
    zoomy=1/math.tan(fov/2)
    zoommatrix=np.matrix([[zoomy, 0, 0, 0],
    [0, zoomy, 0, 0],
    [0,0,1.02, -20.20],
    [0,0,1,0]
    ])
    pclip=zoommatrix*pcam
    #print "my pclip ",pclip
    temp=np.where(pclip<pclip[3])
    temp=np.where(temp>pclip[3])
    temp=np.asarray(temp)
    if temp.size !=0:   #INVALID
        #print "i don't draw it"
        return False
    pcanon=pclip/pclip[3]
    #print pcanon
    #print pcanon[0][0]
    #print pcanon[1][0]
    #print pcanon[3][0]
    dropz=np.matrix([[pcanon.item(0)],[pcanon.item(1)],[pcanon.item(3)]])
    #print dropz
    canonmatrix=np.matrix([[500/2.0, 0, 500/2],
    [0, -500/2, 500/2],
    [0,0,1]
    ])
    pscreen=canonmatrix*dropz
    #print pscreen
    if u==0:
        mylist.append([pscreen.item(0),pscreen.item(1),pscreen.item(2)])
    if u==1:
        mylist.append([pscreen.item(0),pscreen.item(1),pscreen.item(2)])

  #print "i return ", mylist
  carx+=0.001
  return mylist

def getMyPoints(s, xoffest, zoffset, spinhouse):
  mylist=[]
  global transz
  global transx
  global transy
  global rotateangle
  global carx
  global currenttire
  for u in range(2):
    x=0
    y=0
    z=0
    if u==0:
        x=s.start.x
        y=s.start.y
        z=s.start.z
    if u==1:
        x=s.end.x
        y=s.end.y
        z=s.end.z
    startpoint=np.matrix([[x, y, z, 1.0]], dtype=np.float64).T  #this changes the zoom
    #rotateangle=math.pi/2.0
    #print rotateangle
    rotatematrix=np.matrix([[math.cos(spinhouse), 0.0, -1.0*math.sin(spinhouse), 0.0],
    [0.0,1.0, 0.0, 0.0],
    [math.sin(spinhouse), 0.0, math.cos(spinhouse), 0.0],
    [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float64)
    transMatrix=np.matrix([[1, 0.0, 0, transx+xoffest],
    [0.0,1,0.0,transy],
    [0.0,0.0,1,transz+zoffset],
    [0.0,0.0,0.0,1]],dtype=np.float64)
    #print startpoint,"startpoint", startpoint.shape
    #print rotatematrix, "rotatematrix", rotatematrix.shape
    #print transMatrix, " transmatrix", transMatrix.shape
    pworld=transMatrix*rotatematrix*startpoint
    #print "this my pworld ", pworld
    cameraposition=np.matrix([[1,0.0,0,-3],[0,1,0,-1], [0,0,1,40],[0,0,0,1]], dtype=np.float64)
    cameraangle=math.radians(rotateangle)
    rotatecamera=np.asarray([[math.cos(cameraangle), 0.0, -1.0*math.sin(cameraangle),0],
    [0.0, 1.0, 0.0, 0.0],
    [math.sin(cameraangle), 0.0, math.cos(cameraangle), 0.0],
    [0.0,0.0,0.0,1.0]],dtype=np.float64)


    pcam=rotatecamera*cameraposition*pworld
    #print "this is my pcam" ,pcam
    fov=pi/3
    zoomy=1/math.tan(fov/2)
    zoommatrix=np.matrix([[zoomy, 0, 0, 0],
[0, zoomy, 0, 0],
[0,0,1.02, -20.20],
[0,0,1,0]
    ])
    pclip=zoommatrix*pcam
    #print "my pclip ",pclip
    temp=np.where(pclip<pclip[3])
    temp=np.where(temp>pclip[3])
    temp=np.asarray(temp)
    if temp.size !=0:   #INVALID
        dude=[]
        dude.append([s.start.x, s.start.y, s.start.z])
        dude.append([s.end.x, s.end.y, s.end.z])
        #print "i don't draw it"
        return False
    pcanon=pclip/pclip[3]
    #print pcanon
    #print pcanon[0][0]
    #print pcanon[1][0]
    #print pcanon[3][0]
    dropz=np.matrix([[pcanon.item(0)],[pcanon.item(1)],[pcanon.item(3)]])
    #print dropz
    canonmatrix=np.matrix([[500/2.0, 0, 500/2],
    [0, -500/2, 500/2],
    [0,0,1]
    ])
    pscreen=canonmatrix*dropz
    #print pscreen
    if u==0:
        mylist.append([pscreen.item(0),pscreen.item(1),pscreen.item(2)])
    if u==1:
        mylist.append([pscreen.item(0),pscreen.item(1),pscreen.item(2)])
  #print "i return ", mylist
  return mylist
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
global transz
global transx
global transy
global rotateangle
global tirespin

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")

#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
linelist = loadHouse()
carlist=loadCar()
tirelist=loadTire()

#Loop until the user clicks the close button.
while not done:

    # This limits the while loop to a max of 100 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    #Controller Code#
    #####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done=True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        #print "s is pressed"
        transz+=(1.0*math.cos(math.radians(rotateangle)))
        transx+=(1.0*math.sin(math.radians(rotateangle)))
    if pressed[pygame.K_w]:
        #print "w is pressed"
        transz-=(1.0*math.cos(math.radians(rotateangle)))
        transx-=(1.0*math.sin(math.radians(rotateangle)))
    if pressed[pygame.K_r]:#up
        #print "r is pressed"
        transy-=1
    if pressed[pygame.K_f]:#down
        #print "f is pressed"
        transy+=1
    if pressed[pygame.K_a]:#left
        #print("a is pressed")
        #print rotateangle
        transx+=(1.0*math.cos(math.radians(rotateangle)))
        transz-=(1.0*math.sin(math.radians(rotateangle)))
    if pressed[pygame.K_d]:#right
        #print("d is pressed")
        transx-=(1.0*math.cos(math.radians(rotateangle)))
        transz+=(1.0*math.sin(math.radians(rotateangle)))
    if pressed[pygame.K_q]: #rotate
        #print ("q is pressed")
        #print rotateangle
        rotateangle-=1
    if pressed[pygame.K_e]:
        #print("e is pressed")
        rotateangle+=1
    if pressed[pygame.K_h]:
        rotateangle=0
        transx=0
        transy=0
        transz=0
        carx=0
        tirespin=0
    #Viewer Code#
    #####################################################################

    #BOGUS DRAWING METHOD SO YOU CAN SEE THE HOUSE WHEN YOU START UP
    for s in linelist:
        #print s.start.x, "before"
        temp=getMyPoints(s, 0, -15, 0)
        if not temp:
            continue
        #print temp[0][0], "after"
        pygame.draw.line(screen, BLUE, (temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]))
    for s in linelist:
        temp=getMyPoints(s, 15,-15, 0)
        if not temp:
            continue
        #print temp[0][0], "after"
        pygame.draw.line(screen, BLUE, (temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]))
    for s in linelist:
        temp=getMyPoints(s, 15, 15, pi)
        if not temp:
            continue
        #print temp[0][0], "after"
        pygame.draw.line(screen, BLUE, (temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]))
    for s in linelist:
        temp=getMyPoints(s, 0,15, pi)
        if not temp:
            continue
        #print temp[0][0], "after"
        pygame.draw.line(screen, BLUE, (temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]))
    for s in carlist:
        temp=drawMyCar(s)
        if not temp:
            continue
        #print temp[0][0], "after"
        pygame.draw.line(screen, GREEN, (temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]))
    for s in tirelist:
      for dude in range(4):
        currenttire=dude
        #print currenttire
        temp=drawMyWheels(s)
        if not temp:
            continue
        #print temp[0][0], "after"
        pygame.draw.line(screen, RED, (temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]))

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
