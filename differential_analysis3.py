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

