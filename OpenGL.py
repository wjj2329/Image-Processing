import sys
import math

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
transx=0
transy=0
transz=-20
orthox1=-20
orthoy1=20
orthox2=-20
orthoy2=20
near=1
far=50
rotateangle=0
perspective=True
var=0.0
angle=0.0






def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def drawCar():
	glLineWidth(2.5)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-3, 2, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 2, 2)
	#Back Side
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 2, -2)
	#Connectors
	glVertex3f(-3, 2, 2)
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, -2)
	glEnd()

def drawTire():
	glLineWidth(2.5)
	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-1, .5, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, .5, .5)
	#Back Side
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, .5, -.5)
	#Connectors
	glVertex3f(-1, .5, .5)
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, -.5)
	glEnd()


def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()
def drawcar(dude):

    global var
    global angle
    glClear (GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslate(-20,0,30)
    glRotate(180,0,1,0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0,0,30)
    glRotate(180,0,1,0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(20,0,30)
    glRotate(180,0,1,0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    drawHouse()
    glTranslate(-20, 0 , 0)
    drawHouse()
    glPopMatrix()
    glPushMatrix()
    glTranslate(20, 0, 0)
    drawHouse()
    glPopMatrix()
    var+=0.01
    angle+=25
    glPushMatrix()
    glTranslate(var,0.20,10)
    drawCar()
    glPopMatrix()
    #tire back left
    glPushMatrix()
    glTranslate(var-2.0, 0.0, 8.0)
    glRotate(math.radians(-angle),0,0,1)
    drawTire()
    glPopMatrix()
    #tireback right
    glPushMatrix()
    glTranslate(var-2.0, 0.0, 12.0)
    glRotate(math.radians(-angle),0,0,1)
    drawTire()
    glPopMatrix()

    #tire top left
    #glMatrixMode(GL_MODELVIEW);
    glPushMatrix()
    glTranslate(var+2.0, 0.0, 8.0)
    glRotate(math.radians(-angle),0,0,1)
    drawTire()
    glPopMatrix()
    #tire top right
    glPushMatrix()
    glTranslate(var+2.0, 0.0, 12.0)
    glRotate(math.radians(-angle),0,0,1)
    drawTire()
    glPopMatrix()

    #print var
    glutTimerFunc(5,drawcar,0)
    glFlush ()


def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    glRotated(rotateangle,0,1,0)
    glTranslated(transx,transy,transz)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  #gl
    if perspective==True:
      gluPerspective(100,1,1,90)
    else:
      glOrtho(orthox1, orthoy1, orthox2, orthoy2, near, far)
    #Your Code Here

    glMatrixMode(GL_MODELVIEW)

    drawcar(0)
    glFlush ()
# push and pop matrices
def keyboard(key, x, y):
    global glux
    global gluy
    global transz
    global transx
    global transy
    global rotateangle
    global perspective
    global near
    global far
    global orthox1
    global orthoy1
    global orthox2
    global orthoy2
    global var
    global angle
    if key == chr(27):
        import sys
        sys.exit(0)
    if key=='a':
           transx+=(1.0*math.cos(math.radians(rotateangle)))
           transz+=(1.0*math.sin(math.radians(rotateangle)))
           print "i do a with angle",rotateangle ," ", (1.0*math.cos(math.radians(rotateangle))), " ",(1.0*math.tan(math.radians(rotateangle)))
    if key=='d':
        transx-=(1.0*math.cos(math.radians(rotateangle)))
        transz-=(1.0*math.sin(math.radians(rotateangle)))
        print "i do d",(1.0*math.cos(math.radians(rotateangle))), " ",(1.0*math.tan(math.radians(rotateangle)))
    if key=='w':
        transz+=(1.0*math.cos(math.radians(rotateangle)))
        transx-=(1.0*math.sin(math.radians(rotateangle)))

        print "i do w", (1.0*math.cos(math.radians(rotateangle))), " ", (1.0*math.sin(math.radians(rotateangle)))
    if key=='s':
        transz-=(1.0*math.cos(math.radians(rotateangle)))
        transx+=(1.0*math.sin(math.radians(rotateangle)))

        print "i do s", (1.0*math.cos(math.radians(rotateangle)))," ", (1.0*math.sin(math.radians(rotateangle)))
    if key=='q':
        print "i do q"
        rotateangle-=3
    if key=='e':
        print "i do e",rotateangle
        rotateangle+=3
    if key=='r':
        print "i do r"
        transy-=1
    if key=='f':
        print "I do f"
        transy+=1
    if key=='h':
        transx=0
        transy=0
        transz=-20
        rotateangle=0
        var=0.0
        angle=0.0
        print "i do h"
    if key=='o':
        perspective=False
        print "i do o"
    if key=='p':
        perspective=True
        print "i do p"
    #Your Code Here

    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
