from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.misc import imsave
from numpy.linalg import inv

#Your bilateral interpolation function
'''
def interpolate(image, scalex, scaley):
    newpic=np.copy(image)
    for x in range(image.shape[0]):
     for y in range(image.shape[1]):
      for color in range(image[x,y].size):
        tempx=x/scalex
        tempy=y/scaley
        upleftpix=image[int(math.floor(tempx)), int(math.floor(tempy)),color]
        uprightpix=image[int(math.floor(tempx+1)), int(math.floor(tempy)),color]
        downleftpix=image[int(math.floor(tempx)), int(math.floor(tempy+1)),color]
        downrightpix=image[int(math.floor(tempx+1)), int(math.floor(tempy+1)),color]
        totalx1=(math.floor(tempx+1)-tempx)*upleftpix+(tempx-math.floor(tempx))*uprightpix
        totalx2=(math.floor(tempx+1)-tempx)*downleftpix+(tempx-math.floor(tempx))*downrightpix
        newpic[x,y,color]=(math.floor(tempy+1)-tempy)*totalx1+(tempy-math.floor(tempy))*totalx2
    return newpic
'''
def interpolate(image, tempx, tempy, x, y, color,temp):
        upleftpix=temp[int(math.floor(tempx)), int(math.floor(tempy)),color]
        uprightpix=temp[int(math.floor(tempx+1)), int(math.floor(tempy)),color]
        downleftpix=temp[int(math.floor(tempx)), int(math.floor(tempy+1)),color]
        downrightpix=temp[int(math.floor(tempx+1)), int(math.floor(tempy+1)),color]
        totalx1=(math.floor(tempx+1)-tempx)*upleftpix+(tempx-math.floor(tempx))*uprightpix
        totalx2=(math.floor(tempx+1)-tempx)*downleftpix+(tempx-math.floor(tempx))*downrightpix
        image[x,y,color]=(math.floor(tempy+1)-tempy)*totalx1+(tempy-math.floor(tempy))*totalx2


filename = "test.png"
im = imread(filename)

h,w,_ = im.shape

result = np.zeros((int(2.3*h),(int(2.3*w)),3), dtype="uint8")

result[0:h,0:w,:] = im #Temporary line, you can delete it

#Write code that scales the image by a factor of 2.3
#It should call interpolate.

#Your Code Here
temp=np.copy(result)
for x in range(result.shape[0]):
     for y in range(result.shape[1]):
      for color in range(result[x,y].size):
        tempx=x/2.3
        tempy=y/2.3
        interpolate(result, tempx, tempy,x, y, color, temp)
        
#result=interpolate(result, 2.3,2.3)

        
plt.imshow(result,vmin=0)
plt.show()