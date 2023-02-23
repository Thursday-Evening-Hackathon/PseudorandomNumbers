''' Algorithm taken (and translated to Python) from https://de.wikipedia.org/wiki/Xorshift.
    (Adrian) '''
import numpy as np
import matplotlib.pyplot as plt

x32 = np.int32(314159265);
def xorshift32():
    global x32
    x32 ^= x32 << 13
    x32 ^= x32 >> 17
    x32 ^= x32 << 5
    return x32

rndnums = []
for i in range(100000):
    rndnums += [xorshift32()]

plt.plot(rndnums, linestyle='none', marker='.')
plt.show()