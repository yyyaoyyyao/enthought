from numpy import linspace, pi, sin, cos
from pylab import plot, subplot, cm, imshow, xlabel, ylabel, title, grid, \
                  axis, show, savefig, tight_layout

# The following import *is* needed in PyLab.
# The PyLab version of 'imread' does not read JPEGs.
from scipy.misc.pilutil import imread

x = linspace(0, 2*pi, 101)
s = sin(x)
c = cos(x)

# 'flatten' creates a 2D array from a JPEG.
img = imread('dc_metro.jpg', flatten=True)

subplot(2,2,1)
plot(x, s, 'b-', x, c, 'r+')
axis('tight')
subplot(2,2,2)
plot(x, s)
grid()
xlabel('radians')
ylabel('amplitude')
title('sin(x)')
axis('tight')

subplot(2,2,3)
imshow(img, extent=[-10, 10, -10, 10], cmap=cm.winter)
tight_layout()
show()
savefig('plotting.png')