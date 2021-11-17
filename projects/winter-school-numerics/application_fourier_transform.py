""" Exercise for 2d-Fourier transform

    Starting from an electron interferogram, the underlying 2d 
    cosine function (as an approximation) is to be reconstructed 
    using Fourier analysis
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fftshift, fft2
from PIL.Image import open as image_open

def reconstruction(event):
    """ Stellt eine Kosinusfunktion mit den durch das Maus-Klick-Event
        angegebenen Frequenzen dar
    """
    # keine Berechnung wenn Zoommodus bzw. falscher Plotbereich
    toolbar = plt.get_current_fig_manager().toolbar
    if toolbar.mode == '' and event.inaxes == ax2:
        x = np.linspace(-dim/2*scale_pos, dim/2*scale_pos, dim)[np.newaxis, :] 
        y = x.T
        cos_img = np.cos(2*np.pi*(event.xdata*x + event.ydata*y))
    
        if not ax4.get_visible():
            ax4.set_visible(True)
    
        plot_im(ax4, cos_img, dim, scale_pos, "reconstruction")
        plt.gcf().canvas.draw()
    
def plot_im(ax, bilddaten, dim, scale, plottitle, xl="x [nm]", yl="y [nm]"):
    """ Anzeigen der Bilddaten und setzen von Beschriftungen

        zeichnet mittels 'imshow' die Bilddaten 'bilddaten' mit Grenzen
        [-dim/2*scale, dim/2*scale] x[-dim/2*scale, dim/2*scale] in den 
        entsprechenden Plotbereich 'ax' mit Titel 'plottitle' und 
        Achsenbeschriftung (xl, yl) ein.
    """
    ax.images = []                                  # entferne alle Bilder 
    ax.imshow(bilddaten[::-1,:], interpolation='nearest', cmap=plt.cm.gray,
           extent=(-dim/2*scale, dim/2*scale, -dim/2*scale, dim/2*scale))
    ax.set_xlabel(xl)            
    ax.set_ylabel(yl)
    ax.set_title(plottitle)
    
def read_image(fname):
    """
    Reads data from image file name.

    input:    fname:      file name of image data
    returns:  img:        2d-array with image data
              xlen:       size of square image in pixels
    """
    img_raw = np.array(image_open(fname), dtype=np.uint8)
    img = np.float64(img_raw)[::-1,:]
    x_len, y_len = img.shape
    assert x_len == y_len,\
          "Image must be of square dimensions!"
    return img, x_len

img, dim = read_image("HologramFringesNoisy.tif")
img_ref, dim_ref = read_image("HologramFringes.tif")

scale_pos = 0.03                    # scale in nm per pixel
scale_feq = 1./(dim*scale_pos)      # k-space-scale in 1/nm per pixel

ft_img = fftshift(fft2(img-img.mean()))   # Fourier transformat
ft_img = abs(ft_img)                      # absolute value of complex numbers  

plt.figure(1, (9, 9))

ax1 = plt.subplot(221)
plot_im(ax1, img, dim, scale_pos, "noisy data")

ax2 = plt.subplot(222)
plot_im(ax2, ft_img, dim, scale_feq, "Fourier transform", 
          xl="$k_x [1/nm]$", yl="$k_y [1/nm]$")

ax3 = plt.subplot(223)
plot_im(ax3, img_ref, dim_ref, scale_pos, "reference data")

ax4 = plt.subplot(224, visible=False)     # plot space invisible

print(" Chose point in plot space 'Fourier transform' by mouse click ")
print(" as x/y-wave number for 2d-cosine.")
print(" Watch the 'reconstruction'.")

plt.connect('button_press_event', reconstruction)
plt.gcf().tight_layout()
plt.show()
