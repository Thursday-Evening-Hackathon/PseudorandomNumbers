import numpy as np
import matplotlib.pyplot as plt
# https://mpmath.org/
# https://github.com/mpmath/mpmath
# pip install mpmath
from mpmath import mp

N = np.arange(1000000, dtype=int)
N[1] = 0

count = 2
while count < len(N):
    a = N[count]
    if a == 0:
        count += 1
        continue
    N[2*a::a] = 0
    count += 1

P = N[N>0]

# SophieGermain
SophieGermainP = []
SafeP = []
for p in P:
    if 2*p+1>=len(N):
        break
    if N[2*p+1]:
        SophieGermainP += [p]
        SafeP += [2*p+1]

denoms = []
for q in SafeP:
    if (q-7)%40==0 or (q-19)%40==0 or (q+17)%40==0:
        denoms += [q]

mydenom = denoms[-1]
print (mydenom)

mp.dps = 1000000
outstr = str(mp.fdiv(1, mydenom))
print(outstr[2:20])
print(outstr[2+mydenom-1:2+mydenom-1+18])

randnums = [int(chr) for chr in list(outstr)[2:2+mydenom-1]]

np.save('MaximallyPeriodicReciprocals_RndNums_Denom998423.npy', randnums)