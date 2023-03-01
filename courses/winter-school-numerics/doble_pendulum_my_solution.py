import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

l = 1

def dphi_func(phi_vector, t):
    g = 10
    phi1, phi2, phi3, phi4 = phi_vector
    A = np.array([[4/3, 1/2*np.cos(phi1-phi2)], 
                  [1/2*np.cos(phi1-phi2), 1/3]])
    b = np.array([-1/2*phi4**2*np.sin(phi1-phi2)-3/2*g*np.sin(phi1), 
                  1/2*phi3**2*np.sin(phi1-phi2)-1/2*g*np.sin(phi2)])
    dphi = np.linalg.solve(A,b)
    return np.array([phi3, phi4, dphi[0], dphi[1]])

t = np.linspace(0,10,1000)
dt = t[1] - t[0]
initial_phi = [np.pi/2+np.pi/3, 0]
initial_dphi = [5, 5]
initial = initial_phi + initial_dphi

result = odeint(dphi_func, initial, t)

position_bar1 = np.array([l*np.sin(result[:,0]), l*np.cos(result[:,0])])
position_bar2 = position_bar1 + np.array([l*np.sin(result[:,1]), l*np.cos(result[:,1])])

# Animation
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(2, -2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, position_bar1[0,i], position_bar2[0,i]]
    thisy = [0, position_bar1[1,i], position_bar2[1,i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate, range(1, len(result)),
                              interval=dt*1000, blit=True, init_func=init)
plt.show()
