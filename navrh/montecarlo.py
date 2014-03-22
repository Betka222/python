import random
import math

pi = 3.14

def funkce(x):
    return math.sin(x)

def monte(xmin, xmax, ymin, ymax, N):
    zasah = 0
    S= abs(xmax-xmin)*abs(ymax-xmin)
    hod=0
    while hod<N:
        for i in range (1,N):
            x= random.uniform(xmin, xmax)
            y= random.uniform(ymin, ymax)
            
            hod+=1
            if  y < math.sin(x):
                zasah+=1
    obsah = (zasah/N)*S
    return obsah
    
print("Funkce sin(x) na intervalu (0,pi) X (0,1) uzavira pod krivkou: ") 
print(monte(0, pi, 0, 1, 100));

