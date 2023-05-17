from cProfile import label
from re import U
import numpy as np
import matplotlib.pyplot as plt

d = 2
n = 1 
x = np.random.randn(d,n)
u = np.random.randn(d,n)
u = u/np.linalg.norm(u)
print(x)
print(u)

y = (x.T@u)*u  ## @: matrix multiplication
print(y)
fig,ax = plt.subplots()
ax.plot(x[0,0], x[1,0], label="$\mathbf{x}$")
plt.show