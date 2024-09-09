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


x = np.linspace(-1,8,200)
y_init = np.pi/2              # initial condition



plt.figure()
for k_val in [-1,-0.5,0,0.5,2]:
    inside_func = super_func(k_val)
    y_val = dyff_eqn_soln(inside_func,x,y_init)
    plt.plot(x,y_val/np.pi,label=f"k={k_val}")
plt.legend()
plt.ylabel("y")
plt.xlabel("x/pi")
plt.title("Differential equation: y'=k*sin(y); IV: (x,y)=(-1,pi/2)",weight='bold')
plt.savefig(file_path + 'foo2.jpg', bbox_inches='tight')
plt.show()

