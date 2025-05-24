#3.	Create a 5x5 identity matrix but replace the diagonal with values 1 to 5.
import numpy as np
m=np.eye(5)
for i in range(5):
    m[i,i]=i+1
print(m)
