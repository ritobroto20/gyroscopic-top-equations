from utilities import runge_kutta4,dyff_eqn_soln,createFolder
from utilities import contourIntegral,nthDerivative
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib import style 
import os


# Differential equation of interest
# Change the function to see how different derivatives of the function behaves
def super_func(k=1):
    def wrapper(x,y):
        return k*np.sin(y)
    return wrapper

function1=super_func(2)


def asymptoticBehaviour(func,y_init=0.001):
    x = np.linspace(0.001,(1.701e5),int(1.701e7))
    index_values = [1e7,1.1e7,1.2e7,1.3e7,1.4e7,1.5e7,1.6e7,1.7e7]
    y_values = []
    dy_values = []
    dx = x[0]-x[1]

    y_solution = dyff_eqn_soln(func,x,y_init)
    
    for i in (index_values):
        y_values.append(y_solution[int(i)])

    return (y_values)


def asymptotic(func):
    x = np.linspace(0.001,(1.701e5),int(1.701e7))
    index_values = [1e7,1.1e7,1.2e7,1.3e7,1.4e7,1.5e7,1.6e7,1.7e7]
    y_values = []
    dy_values = []
    dx = 0.01

    for i in index_values:
        y_values.append(func(x[int(i)]))

    return (y_values)


def asymptoticConvergence(y_values):
    N = len(y_values)
    convergence = 0
    temp = []
    for i in range(N-2):
        if abs(y_values[i+1]-y_values[i])>abs(y_values[i+2]-y_values[i+1]):
            temp.append(-1)
        else:
            temp.append(1)


    if (abs(y_values[N-1]-y_values[0])<0.01):
        convergence = -1
    if (abs(y_values[0])>1e300):
        convergence = 1
    if (abs(y_values[N-1]-y_values[0])>0.01):
        convergence = 1     
    
    return convergence



if __name__ == "__main__":
    
    plt.style.use('bmh') 
    file_path = './reports/differential_analysis3/'
    createFolder(file_path)

    function1 = super_func(2)
    y_initial = np.arange(-2.5*np.pi,2.5*np.pi,0.1*np.pi)
    convergence_val = []
    asymptotic_val = []
    for i in y_initial:
        print(i)
        asymptotic_points = asymptoticBehaviour(function1, i)
        asymptotic_coverge_value = asymptoticConvergence(asymptotic_points)
        asymptotic_val.append(asymptotic_points[-1])
        convergence_val.append(asymptotic_coverge_value)

    print("_________________________________________")
    # print(y_initial)
    print(asymptotic_val)
    print(convergence_val)


    fig, ax = plt.subplots()
    scatter = ax.scatter(y_initial,np.arctan(asymptotic_val),c=convergence_val,cmap='viridis',edgecolors='dimgray')

    # produce a legend with the unique colors from the scatter
    legend1 = ax.legend(*scatter.legend_elements(),
                    loc="center right", title="-1: Convergent\n 1: Divergent\n 0: Unkown")
    ax.add_artist(legend1)
    plt.title("Asymptotic behaviour of: y'=2sin(y)",weight="bold")
    plt.xlabel("Y_initial")
    plt.ylabel("arctan( Y_asymptotic )")
    # plt.ylim(0,1.7)
    plt.savefig(file_path + 'foo2.png', bbox_inches='tight')
    plt.show()








