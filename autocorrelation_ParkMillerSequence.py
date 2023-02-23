import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = np.load('ParkMillerSequence.npy')
acf = sm.tsa.stattools.acf(data)
plt.plot(acf)
plt.show()