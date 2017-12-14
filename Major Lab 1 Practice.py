##Paul Heys
##Practice for major 1

import math
4
R = input("Enter the circle radius: ")
r = input("Enter the tube radius: ")

A = 4*math.pi**2*R*r
print "A=",A

B = 4*math.pi**2*R*3*r
print "B=",B

C = (abs(A-B)/B)*100
print "C=",C
