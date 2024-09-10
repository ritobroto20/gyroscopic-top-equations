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
        return k*np.cos(y)
    return wrapper


x = np.linspace(-1,8,200)
# y_init = np.pi/2              # initial condition



plt.figure()
for y_init in [-0.5*np.pi,-0.7*np.pi,-0.3*np.pi,0,0.3*np.pi,1.2*np.pi,1.7*np.pi]:
    inside_func = super_func()
    y_val = dyff_eqn_soln(inside_func,x,y_init)
    plt.plot(x,y_val/np.pi,label=f"y_init={y_init:.1f}")
plt.ylabel("y")
plt.xlabel("x/pi")
plt.title("Differential equation: y'=k*cos(y); k=1",weight='bold')
plt.axhline(y = -0.5, color = 'r', linestyle = ':',label="zeros of cos(y)") 
plt.axhline(y = 1.5, color = 'r', linestyle = ':') 
plt.axhline(y = 2.5, color = 'r', linestyle = ':') 
plt.axhline(y = 0.5, color = 'r', linestyle = ':') 
plt.axhline(y = -1.5, color = 'r', linestyle = ':') 
plt.legend()
plt.savefig(file_path + 'foo.png', bbox_inches='tight')
plt.show()

