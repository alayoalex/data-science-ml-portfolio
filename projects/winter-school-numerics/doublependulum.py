#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:03:54 2020

@author: bittrich
"""
import matplotlib
matplotlib.use("qt5agg")

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

g = 10.

def pendulum(dphi_phi, t):
    dphi1, dphi2, phi1, phi2 = dphi_phi
    M = np.array([[4/3, .5*np.cos(phi1-phi2)],
                  [.5*np.cos(phi1-phi2), 1/3]])
    V = np.array([-.5*dphi2**2*np.sin(phi1-phi2)-3/2*g*np.sin(phi1),
                  .5*dphi1**2*np.sin(phi1-phi2)-.5*g*np.sin(phi2)])
    ddphi = np.linalg.solve(M, V)
    return np.array([ddphi[0], ddphi[1], dphi1, dphi2])

def compute_xy(dphi_phi):
    x1 = np.sin(dphi_phi[:,2])
    y1 = -np.cos(dphi_phi[:,2])
    x2 = x1 + np.sin(dphi_phi[:,3])
    y2 = y1 - np.cos(dphi_phi[:,3])
    return x1, y1, x2, y2

    

dphi_phi0 = np.array([0., 0., np.pi/2, 0.])
t = np.linspace(0, 30., 3000)

dphi_phi = odeint(pendulum, dphi_phi0, t)

#ax = plt.subplot(121)
#ax.plot(t, dphi_phi[:,2])
#ax2 = plt.subplot(122)
#ax2.plot(t, dphi_phi[:,3])
#plt.show()

x1, y1, x2, y2 = compute_xy(dphi_phi)

fig = plt.figure()
ax = plt.subplot(111, aspect="equal")
ln1, = ax.plot([],[])
ln2, = ax.plot([],[])
ln3, = ax.plot([0,x1[0],x2[0]], [0,y1[0],y2[0]], 'ko-', lw=5)

def init():
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.1, 1.1)
    return ln1, ln2, ln3

def update(frame):
    ln1.set_data(x1[:frame+1], y1[:frame+1])
    ln2.set_data(x2[:frame+1], y2[:frame+1])
    ln3.set_data([0,x1[frame],x2[frame]], [0,y1[frame],y2[frame]])
    return ln1, ln2, ln3
    

ani = FuncAnimation(fig, update, frames=range(len(x1)),
                    init_func=init, interval=1,blit=True)

plt.show()