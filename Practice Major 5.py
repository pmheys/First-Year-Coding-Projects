from math import *

class particle1D:

    def __init__(self, m, ro, vo, ao):
        self.m = m
        self.r = ro
        self.v = vo
        self.a = ao

    def getM(self):
        return self.m

    def getR(self):
        return self.r

    def getV(self):
        return self.v

    def getA(self):
        return self.a

    def update(self, dt):

        self.r = self.r + self.v * dt + (0.5) * self.a * dt**2
        self.v = self.v + self.a * dt

    def applySpringForce(self, k):

        self.a = -(k*self.r)/float(self.m)


def runSpringSim(p, cycles, dt, k):

    output = [p.getR()]

    for i in range(cycles):
        p.applySpringForce(k)
        p.update(dt)
        output.append(p.getR())

    return output











        

    
