import numpy as np
import matplotlib.pyplot as plt
## Y = Ax
## Size:Y 2*4, A 2*3, X 3*4,
n = 4
d_X = 3
d_Y = 2

## choose a "true" A
A_true = np.random.randn(d_Y,d_X)

## sample random X
X = np.random.randn(d_X,n)
Y = A_true@X

## calculation of A

A = Y@X.T @ np.linalg.inv(X@X.T)

print(A_true)
print(A)