def backmap1(image, transform):
    
    h,w,_ = im.shape
    
    result = np.zeros((h,w,3), dtype="uint8")
    transform=inv(transform)
    copy=np.copy(image)
    for x in range(result.shape[0]):
     for y in range(result.shape[1]):
      for color in range(result[x,y].size):
        transformationmatrix=np.matrix([[-x, y ,1]])
        newcoords=transformationmatrix*transform
        #print x,y ," becomes ", newcoords[0,0], " ", newcoords[0,1]
        try:
         interpolate(result, newcoords[0,0],newcoords[0,1] ,x, y, color, image)
        except:
            something=0
    return result


from math import sin,cos,pi

filename = "test.png"
im = imread(filename)

transform = np.matrix([[cos(45 * pi/180), -sin(45 * pi/180), w/2],[sin(45 * pi/180),cos(45 * pi/180),-h/5],[0,0,1]])

result = backmap1(im,transform)

plt.imshow(result,vmin=0)
plt.show()
