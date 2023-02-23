import numpy as np

class ParkMiller:
    def __init__(self) -> None:
        self.a = 16807
        self.m = 2**31-1
        self.r = 2836#self.m%self.a
        self.q = 127773#(self.m-self.r)//self.a
    
    def random(self,seed,N):
        y = ((888889999 ^ abs(seed)) | 1)
        self.rnd_arr = np.zeros(N)

        for i in range(N):
            y = self.a*(y%self.q) - self.r*(y//self.q)
            if y < 0:
                y += self.m
                
            self.rnd_arr[i] = y/self.m

        return self.rnd_arr


class ACORN:
    def __init__(self) -> None:

        self.k = 25         # Order k
        self.maxint = 2**30 # Modulus M

        self.ixv1 = np.zeros(self.k+1)
        self.ixv2 = np.zeros(self.k+1)

        return

    def random(self,seed,N):

        self.ixv1[0] = 2**24-seed #inital seed(?) 
        self.ixv2[0] = 0#2**10-seed #inital seed(?)

        rnd_arr = np.zeros(N)

        for j in range(N):
            for i in range(self.k):
                self.ixv1[i+1] =  self.ixv1[i+1]+ self.ixv1[i]
                self.ixv2[i+1] =  self.ixv2[i+1]+ self.ixv2[i]

                if self.ixv2[i+1]>= self.maxint:
                    self.ixv2[i+1]= self.ixv2[i+1]-self.maxint
                    self.ixv1[i+1]= self.ixv1[i+1]+1

                if  self.ixv1[i+1]>=self.maxint:
                    self.ixv1[i+1]= self.ixv1[i+1]-self.maxint

            rnd_arr[j] = (self.ixv1[self.k]+(self.ixv2[self.k]/self.maxint))/self.maxint
            
        return rnd_arr



class MersenneTwister:
    def __init__(self) -> None:
        self.MT = [0]*624
        self.index = 0
       

    def random(self,seed,N):

        self.MT[0] = seed

        for i in range(1,624):
            self.MT[i] = (1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30))+i) & 0xFFFFFFFF

        result = []
        uppermask = 0x80000000
        lowermask = 0x7FFFFFFF

        for _ in range(N//624+1):
            for i in range(624):
                y = (self.MT[i] & uppermask) | (self.MT[(i+1)%624] & lowermask)
                self.MT[i] = self.MT[(i+397)%624] ^(y>>1)
                if y % 2 != 0:
                    self.MT[i] ^= 0x9908B0DF
                result.append(self.extract_number())
            
        return result

    def extract_number(self):
        y = self.MT[self.index]
        y ^= (y >> 11)
        y ^= ((y<<7) & 0x9D2C5680)
        y ^= ((y<<15) & 0xEFC60000)
        y ^= (y >> 18)
        self.index = (self.index+1)%624
        return y