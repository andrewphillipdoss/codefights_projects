#You are given an n x n 2D matrix that represents an image. 
#Rotate the image by 90 degrees (clockwise).

def rotateImage(a):
    n = len(a)-1
    y = []
    x = []
    for j in range(0,len(a)):
        for i in range(0,len(a)):
          x.append(a[abs(i-n)][j])
          while len(x) == len(a):
              y.append(x)
              x = []
    return y
