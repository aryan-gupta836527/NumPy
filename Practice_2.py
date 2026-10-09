import numpy as np

A = np.array([12, 7, 24, 31, 40, 15, 52, 9])

print(A[A%2==0])#Print even numbers
print(A[(A>10)&(A<40)])#Print numbers b/w 10 and 40
print(A*3)
print(f'Mean: {A.mean()}, Standard Deviation: {A.std()}')