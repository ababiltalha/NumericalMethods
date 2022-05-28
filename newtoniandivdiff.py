import numpy as np
import matplotlib.pyplot as plt

def product(i, value, x):
	prod= 1
	for j in range(i):
		prod= prod*(value-x[j])
	return prod

def dividedDiff(x, y, n):

	for i in range(1, n):
		for j in range(n - i):
			y[j][i]= ((y[j][i-1]-y[j+1][i-1]) / (x[j]-x[i + j]))
	return y

def findY(value, x, y, n):
	sum= y[0][0]
	for i in range(1, n):
		sum= sum+(product(i, value, x)*y[0][i])
	return sum


n= 5
y= [[0 for i in range(10)]
		for j in range(10)]
x= [19,22,26,28,30]
vel= [3000,3500,4000,4500,5000]
mass= [1203,1245,1378,1315,1475]

for i in range(n):
    y[i][0] = vel[i]


y=dividedDiff(x, y, n)
# print(y)
print(findY(25, x, y, n))
plt.plot(x, vel)
plt.show()

for i in range(5):
    y[i][0] = mass[i]


y=dividedDiff(x, y, n)
# print(y)
print(findY(25, x, y, n))
# plt.plot(x, mass)

