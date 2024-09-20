from utilities import runge_kutta4,dyff_eqn_soln,createFolder
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib import style 
import os

plt.style.use('bmh') 
file_path = './reports/differential_analysis2/'
createFolder(file_path)

 
# Differential equation of interest
def super_func(k=1):
    def wrapper(x,y):
        return k*(y**2-1)
    return wrapper

print()

x = np.linspace(-4,1,200)       # x range
# y_init = np.pi/2              # initial condition



if __name__ == "__main__":

    plt.figure()
    for y_init in [-2,-1,-0.5,0,0.5,1,1.00006]:
        inside_func = super_func()
        y_val = dyff_eqn_soln(inside_func,x,y_init)
        plt.plot(x,y_val,label=f"y_init={y_init:.1f}")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title("Differential equation: y'=k*(x^2-1); k=1",weight='bold')
    plt.axhline(y = -1, color = 'r', linestyle = ':',label="zeros of (y^2-1)") 
    plt.axhline(y = 1, color = 'r', linestyle = ':') 
    plt.legend() 
    plt.savefig(file_path + 'foo3.png', bbox_inches='tight')
    plt.show()

