import numpy as np
import matplotlib.pyplot as plt

'''
partial distribution function (pdf) f:
    f(x) = e^(-x)
cumulative distr. function F:
    F(x) = 1-e^(-x)
inverse of the cumul. distr. function:
    u := F(x)
    => F^(-1)(u) = ln(1/(1-u)) with u in [0, 1], because 1 is the norm of the pdf
    this is equivalent to sampling ln(1/u)=-ln(u), because u has uniform probability density on [0,1]
'''

u = np.random.rand(100000)
x = -np.log(u)

plt.hist(x)
plt.yscale('log')
plt.show()