import numpy as np
A = np.arange(1, 13)
print(A.reshape(3,-1))
print(A.reshape(2,2,3))
print(A.reshape(-1,2))
print(A.reshape(3,-1).T.shape)