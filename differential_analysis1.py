from utilities import runge_kutta4,dyff_eqn_soln,createFolder
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib import style 
import os

plt.style.use('bmh') 
file_path = './reports/differential_analysis1/'
createFolder(file_path)
 

# Differential equation of interest
def super_func(k=1):
    def wrapper(x,y):
        return k*np.sin(y)
    return wrapper

def function2(x,y):
    if (y<5):
        return y
    elif (y>=5 or y<10):
        return y

# differential function
def super_func2(k=1):
    def wrapper(x,y):
        return k/np.sin(y)
    return wrapper

x = np.linspace(0,1,200)
y_init = np.pi/2              # initial condition



plt.figure()
for k_val in [-1,-0.5,0,0.5,1]:
    inside_func = super_func2(k_val)
    y_val = dyff_eqn_soln(inside_func,x,y_init)
    if k_val == 1:
        y_stored = y_val
    plt.plot(x,y_val,label=f"k={k_val}")
plt.legend()
plt.ylabel("y")
plt.xlabel("x")
plt.title("Differential equation: y'=k*cosec(y); IV: (x,y)=(0,pi/2)",weight='bold')
plt.savefig(file_path + 'foo3.jpg', bbox_inches='tight')
plt.show()

print(y_stored[99]/2)