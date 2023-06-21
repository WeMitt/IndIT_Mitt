#import Befehl und Bibliotheken
#import random as r 
#from random import randint as r

import numpy as np
import scipy as sy
import matplotlib.pyplot as mp

koord={0:0}
x_koord=[]
y_koord=[]
g_nau=float(input("Gewünschte Genauigkeit:"))

step=0
while step<=360:
    koord[step]=np.sin((step*np.pi)/180)
    step=step+g_nau

for x_k, y_k in koord.items():
    x_koord.append(x_k)
    y_koord.append(y_k)

mp.plot(x_koord,y_koord)
mp.grid(True)
mp.title('Plot einer Sinusfunktion')
mp.xlabel('Winkel in Grad')
mp.ylabel('sin(x)')
mp.show()