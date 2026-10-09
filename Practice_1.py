import numpy as np

students = np.array([
    [18, 85, 90],
    [19, 65, 70],
    [18, 92, 88],
    [20, 55, 60],
    [19, 78, 82]
])

print(students.shape)
print(students.ndim)
print(students.size)
print(students[:,1])
print(students[students[:,1]>75])
print(students[students[:,2]>80])