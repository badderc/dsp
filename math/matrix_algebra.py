# Matrix Algebra

"""Linear Algebra Worksheet"""

import numpy as np

A = np.array([1,2,3,2,7,4]).reshape(2,3)
B = np.array([1,-1,0,1]).reshape(2,2)
C = np.array([5,-1,9,1,6,0]).reshape(3,2)
D = np.array([3,-2,-1,1,2,3]).reshape(2,3)
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])[:,None]

# MATRIX DIMENSIONS
print('Dim of A: ' + str(A.shape))
    # (2, 3)
print('Dim of B: ' + str(B.shape))
    # (2, 2)
print('Dim of C: ' + str(C.shape))
    # (3, 2)
print('Dim of D: ' + str(D.shape))
    # (2, 3)
print('Dim of u: ' + str(u.shape))
    # (4,)
print('Dim of w: ' + str(w.shape))
    # (4, 1)

print('\n')

# VECTOR OPERATIONS
print('u+v= ' + str(u + v))
    # [ 9  7 -4  9]
print('u-v= ' + str(u - v))
    # [ 3 -3 -2  1]
print('alpha*u= ' + str(6*u))
    # [ 36  12 -18  30]
print('u dot v= ' + str(np.dot(u,v)))
    # 51
print('norm of u= ' + str(np.linalg.norm(u)))
    # 8.60232526704
print('\n')

# MATRIX OPERATIONS
# print('A+B =' + str(A+B))
    # NOT DEFINED
print('A-C^T= ' + str(A - C.transpose()))
    # [[-4 -7 -3]
    # [ 3  6  4]]
print('C^T+3*D= ' + str(C.transpose() + 3*D))
    # [[14  3  3]
    # [ 2  7  9]]
print('BA= ' + str(np.dot(B,A)))
    # [[-1 -5 -1]
    # [ 2  7  4]]
# print('BA^T= ' + str(np.dot(B,A.transpose)))
    # NOT DEFINED

