from __future__ import division
from scipy import integrate
import random
import math

pi = 3.14

def funkce(x):
    return math.sin(x)

def monte(xmin, xmax, ymin, ymax, N):
    zasah = 0
    S = abs(xmax-xmin)*abs(ymax-xmin)
    
    for i in range (1,N):
        x= random.uniform(xmin, xmax)
        y= random.uniform(ymin, ymax)
        
        if  y < funkce(x):
            zasah+=1
    
    obsah = (zasah/N)*S
    return obsah

xmin = 0
xmax = pi
ymin = 0
ymax = 1
    
print("Funkce sin(x) na intervalu (0,pi) X (0,1) uzavira podle MC: ") 
print(monte(xmin, xmax, ymin, ymax, 100));

print("\nFunkce sin(x) na intervalu (0,pi) X (0,1) uzavira pod krivkou: ") 
print(integrate.quad(lambda x: funkce(x), 0, pi)[0])