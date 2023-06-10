import numpy as np
import matplotlib.pyplot as plt


x = np.array([, , , , ])
y = np.array([10.17, 10.6, 11.52, 11.66, 10.34])

print(np.mean(x-y))

xbar = np.mean(x)
ybar = np.mean(y)
numerator=np.sum(x*y-x*ybar)
denominator=np.sum(x*x-x*xbar)
m = 1
#numerator/denominator
print ("slope: ", m)
b = ybar-m*xbar
print ("y intercept: ", b)
line = m*x +b


fit_line = plt.plot(x, line, color='black', label="")
plt.legend(loc='lower right')
plt.scatter(x,y)
plt.xlabel("Instrumental Magnitude")
plt.ylabel("Apparent Magnitude")
plt.show()

residual = y - line
resid_line = x*0
plt.scatter(x, residual)
plt.title("residual plot")
plt.ylabel("redidual")
plt.plot(x,resid_line, color='black', label="line of zero residual")
plt.legend()
plt.show()
