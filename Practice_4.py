import numpy as np
A = np.arange(1, 13)
print(A.reshape(3,-1))#Reshape A into a 2D array with 3 rows.
print(A.reshape(2,2,3))#Reshape A into a 3D array with shape (2, 2, 3).
print(A.reshape(-1,2))#Create a 2D array with 2 columns
print(A.reshape(3,-1).T.shape)#Transpose the result from task 1 and print its new shape.