'''
A few gaussian curves
'''

import matplotlib.pyplot as plt
import numpy as np

def gaussian(a, b, c, d, x):
    '''
    Gaussian function
    a = maximum
    b = center
    c = standard deviation??
    d = minumum
    '''
    return a*np.exp(-((x-b)**2)/(2*c**2)) + d

print(gaussian(1, 2, 3, 4, 5))


X = np.linspace(0, 100)

Y = [gaussian(100, 50, 25, 1, x) for x in X]
plt.plot(X, Y)

#Y = [gaussian(1, 50, 1, 1, x) for x in X]
#plt.plot(X, Y)
#
#Y = [gaussian(1, 1, 50, 1, x) for x in X]
#plt.plot(X, Y)
#
#Y = [gaussian(1, 1, 1, 50, x) for x in X]
#plt.plot(X, Y)

plt.legend()
plt.show()
