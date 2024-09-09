import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy as sp
from matplotlib import style 
import os


plt.style.use('bmh') 


def runge_kutta4(f,x,y,h):
    k1 = h * f(x,y)
    k2 = h * f(x+h/2,y+k1/2)
    k3 = h * f(x+h/2,y+k2/2)
    k4 = h * f(x+h,y+k3)
    y_new = y + k1/6 + k2/3 + k3/3 + k2/6
    return y_new

# for k in [-1,-0.5,0,1]

def dyff_eqn_soln(func,x_arr,y_inital):
    y = np.zeros(len(x_arr))
    y[0] = y_inital
    h = x_arr[1] - x_arr[0]
    for i in range(len(x_arr)-1):
        y[i+1] = runge_kutta4(func,x_arr[i],y[i],h)
        # print(y[i])
    return y

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


# Animation part
if __name__=="__main__":
    fig, ax = plt.subplots()
    t = np.linspace(0, 3, 40)
    g = -9.81
    v0 = 12
    z = g * t**2 / 2 + v0 * t

    v02 = 5
    z2 = g * t**2 / 2 + v02 * t

    scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
    line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
    ax.set(xlim=[-1, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
    ax.legend()


    def update(frame):
        # for each frame, update the data stored on each artist.
        x = t[:frame]
        y = z[:frame]
        # update the scatter plot:
        data = np.stack([x, y]).T
        scat.set_offsets(data)
        # update the line plot:
        line2.set_xdata(t[:frame])
        line2.set_ydata(z2[:frame])
        return (scat, line2)


    ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=45)
    plt.show()
