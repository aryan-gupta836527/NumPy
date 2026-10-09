import numpy as np
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
print(np.concatenate((A,B),axis=0))#Combine vertically
print(np.concatenate((A,B),axis=1))#Combine horizontally
print(np.split(np.concatenate((A,B),axis=1),2,axis=1))#Split the horizontal result into two equal parts along axis=1