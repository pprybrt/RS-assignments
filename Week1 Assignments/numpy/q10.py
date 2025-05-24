#10.	Append only even numbers from [4, 5, 6] to arr = np.array([1, 2, 3]).

import numpy as np
arr=np.array([1,2,3])
n=np.array([4,5,6])
even=[i for i in n if n%2==0]
arr=np.append(arr,even)
print(arr)
