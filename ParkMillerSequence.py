import numpy as np
a = 16807
m = 2**31-1
q = 127773
r = 2836

seed = 1228

y = np.int32((888889999^abs(seed))|1)

def rndnum():
    global y
    y = a*(y%q)-r*(y//q)
    y = y+m if y<0 else y
    return y

ylist = [rndnum() for i in range(1000000)]
np.save('ParkMillerSequence.npy', ylist)