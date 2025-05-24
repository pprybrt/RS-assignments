# #5.	Extract unique rows from a 2D array.
# [[1, 2], 
#  [3, 4], 
#  [1, 2]]

import numpy as np
arr=np.array([[1, 2],[3, 4],[1, 2]])
uniq=[]
for row in arr:
    if list(row) not in uniq:
        uniq.append(list(row))
uniq=np.arr(uniq)
print(uniq)
