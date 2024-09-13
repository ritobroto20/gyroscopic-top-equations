from utilities import runge_kutta4,dyff_eqn_soln,createFolder
from utilities import contourIntegral,nthDerivative
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib import style 
import os

plt.style.use('bmh') 
file_path = './reports/differential_analysis2/'
createFolder(file_path)


# Differential equation of interest
# Change the function to see how different derivatives of the function behaves
def super_func(k=1):
    def wrapper(x,y):
        return k*np.arctan(y)
    return wrapper

function1=super_func(2)


# for i in range(1,8):
#     print(f"{i}-th derivative of f(x) at y=10:   ",round(nthDerivative(function,i,10).real,4))
# print("...........................")
# print()


# x=np.linspace(-100,100,5000)
# y=np.arctan(x)
# plt.figure()
# plt.plot(x,y)
# plt.show()

def asymptoticBehaviour(func):
    x = np.linspace(0.001,(1.701e5),int(1.701e7))
    index_values = [1e7,1.1e7,1.2e7,1.3e7,1.4e7,1.5e7,1.6e7,1.7e7]
    y_init = 0.001
    y_values = []
    dy_values = []
    dx = x[0]-x[1]
    print(dx)

    y_solution = dyff_eqn_soln(func,x,y_init)
    
    for i in (index_values):
        
        dy_dx = (y_solution[int(i)+1]-y_solution[int(i)])/dx
        y_values.append(y_solution[int(i)])
        dy_values.append(dy_dx)

    return (y_values,dy_values)


def some_function(x):
    return np.exp(x)

def asymptotic(func):
    x = np.linspace(0.001,(1.701e5),int(1.701e7))
    index_values = [1e7,1.1e7,1.2e7,1.3e7,1.4e7,1.5e7,1.6e7,1.7e7]
    y_values = []
    dy_values = []
    dx = 0.01

    for i in index_values:
        dy_dx=(func(x[int(i+1)])-func(x[int(i)]))/dx
        y_values.append(func(x[int(i)]))
        dy_values.append(dy_dx)

    return (y_values,dy_values)

A = asymptotic(some_function)
print(A[0][0]-A[0][-1])


