import numpy as np

values = [56.0, 0.0, 4.4, 68.0, 1.2, 104.0, 52.0, 8.0, 1.8, 135.0, 99.0, 0.9]
vector = np.array(values)
A = vector.reshape(3, 4)
print(A)
B = np.sum(A, axis=0)
print(B)
C =  A / B * 100
print(C)
x=np.array([[[1,2],[2,3],[3,4]],[[3,2],[4,5],[5,6]]])
print(x)
print(x.shape)

a=np.random.randn(1,3)
b=np.random.randn(3,3)

c=a+b

print(c)
print(c.shape)