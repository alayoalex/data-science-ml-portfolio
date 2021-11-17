# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftshift

# define size of data, must be even due to assumptions later on 
# but in general odd is also possible
N = 256
t = np.linspace(0, 2*np.pi, N, endpoint=False) # try without endpoint=False
# select some function
y = np.sin(t)
y = t
y = 1.*(t>np.pi)
#y = 5*np.sin(3*t)*np.cos(t) + np.cos(2*t)*np.sin(t) + .2

# Fourier transform of y (FFT)
fty = fft(y)
ftys = fftshift(fty)       # shift array to get symmetrical data around k=0
absmax = abs(fty).max()    # used for plotting only
k = np.arange(-N//2, N//2) # wave numbers for symmetrical plot (needs even N) 

def update_reconstruction(event):
    if event.inaxes == ax_spec:
        # clear collections and patches for spectrum plot
        ax_spec.collections = []
        ax_spec.patches = []
        
        # get new kmax
        kmax = int(round(abs(event.xdata)))
        # mark the wave number area
        ax_spec.fill([-kmax,-kmax,kmax,kmax], 
                     [0,absmax,absmax,0], color='g', alpha=.3)
        ax_spec.vlines([-kmax, kmax], ymin=0, ymax=absmax, color='r')
        
        # for new reconstruction take a fresh copy and zero out some values
        newft = fty.copy()
        if kmax>0:
            newft[kmax+1:-kmax] = 0 # all values with abs(k)>kmax -> 0
        else:
            newft[1:] = 0 # special case -> only one value is nonzero
        lcurrrec.set_data(t, ifft(newft).real)
        # now also abs(k)<kmax should go to zero
        if kmax>0: # if kmax = 0 nothing to do
            newft[:kmax] = 0
            if kmax>1: # if kmax = 1 we are also done here
                newft[-kmax+1:] = 0
        lcurrfreq.set_data(t, ifft(newft).real)
        plt.gcf().canvas.draw()
        
# plot some initial data and setup lines for current_freq and current_rec
ax_time = plt.subplot(121)
ax_time.plot(t, y, lw=1)
ax_time.set_xlabel('t')
ax_time.set_ylabel('y(t)')
ymax = max(abs(y.min()),y.max())+.2
ax_time.set_ylim(-ymax, ymax)
lcurrfreq, = ax_time.plot([],[], 'r-')
lcurrrec, = ax_time.plot([],[], 'g-')

ax_spec = plt.subplot(122)
ax_spec.stem(k, abs(ftys))
ax_spec.set_xlim(-N/15, N/15) # confine to small area to actually see something
ax_spec.set_xlabel('k')
ax_spec.set_ylabel('$|Y(k)|$')
# connect update event function
plt.connect('button_press_event', update_reconstruction)
plt.show()

