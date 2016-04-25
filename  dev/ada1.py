import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
#help(random.normal)
mu, sigma = 50, 25
s = random.normal(mu,sigma,100000)
count, bins, ignored = plt.hist(s, 50, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
          linewidth=2, color='r')
plt.show()
