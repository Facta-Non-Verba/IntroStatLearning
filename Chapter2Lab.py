#Going through the lab in ISLR Chapter 2, trying to use Numpy to do everything
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#2.3.1 Basic Commands
x = np.array([1, 3, 2, 5])
print(x)

x = np.array([1, 6, 2])
y = np.array([1, 4, 3])
print(len(x))
print(len(y))
print(x+y)

x = np.array([1, 2, 3, 4])
y = np.reshape(x, (2, 2))
print(y)

print(np.sqrt(y))

x = np.random.normal(0, 1, 50)
y = x + np.random.normal(50, 0.1, 50)
print(np.corrcoef(x, y))

np.random.seed(1303)
x = np.random.normal(0, 1, 10)
print(x)
print("The mean is " + str(np.mean(x)))
print("The variance is " + str(np.var(x)))
print("The standard devation is " + str(np.std(x)))


#2.3.2 Graphics
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
plt.plot(x, y, 'o')
plt.xlabel("this is the x-axis")
plt.ylabel("this is the y-axis")
plt.title("Plot of X vs Y")
#plt.show()

x = np.arange(1, 11)
print(x)
x = np.linspace(-1 * np.pi, np.pi, 50)
print(x)
y = x
ufunc = np.frompyfunc(lambda x, y: np.cos(y)/(1 + x*x), 2, 1)
f = ufunc.outer(x, y)
plt.clf()
plt.contour(x, y, f)
plt.show()
