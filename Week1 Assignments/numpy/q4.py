#4.	Given a 5x5 random array, extract only the border elements (first/last row/column).
#(write the code so it is suitable for any given 5x5 array)


import numpy as np
a=np.random.rand(5,5)
top=a[0]
bottom=a[4]
left=a[1:4,0]
right=a[1:4,4]
brdrs=np.concatenate([top,bottom,left,right])
print("originalarray:\n",a)
print("border elements:\n",brdrs)

