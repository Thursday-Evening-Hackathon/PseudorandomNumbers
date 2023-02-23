a = 16807
m = 2**31-1
q = 127773
r = 2836

seed = 1227
y = (888889999^abs(seed))|1

def rndnum():
    global y
    y = a*(y%q)-r*(y//q)