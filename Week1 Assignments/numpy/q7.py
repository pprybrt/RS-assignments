#7.	Calculate the determinant of a 3x3 matrix without using np.linalg.det.
import numpy as np
m=np.random.randint(0,10,size=(3,3))
det=(m[0,0]*(m[1,1]*m[2,2]-m[1,2]*m[2,1])
     -m[0,1]*(m[1,0]*m[2,2]-m[1,2]*m[2,0])
     +m[0,2]*(m[1,0]*m[2,1]-m[1,1]*m[2,0]))

print(det)