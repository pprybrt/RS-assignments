#2.	Generate an 8x8 checkerboard pattern (alternating 0s and 1s) without using loops   #reference: google and chatgpt

import numpy as np
checkerboard=np.zeros((8,8))
checkerboard[1::2,::2]=1
checkerboard[::2,1::2]=1
print(checkerboard)
