"""
Filter Image
------------

Read in the "dc_metro" image and use an averaging filter
to "smooth" the image.  Use a "5 point stencil" where
you average the current pixel with its neighboring pixels::

              0 0 0 0 0 0 0
              0 0 0 x 0 0 0
              0 0 x x x 0 0
              0 0 0 x 0 0 0 
              0 0 0 0 0 0 0

Plot the image, the smoothed image, and the difference between the
two.

Bonus
~~~~~

Re-filter the image by passing the result image through the filter again. Do
this 50 times and plot the resulting image. 

See :ref:`filter-image-solution`.
"""

from scipy.misc.pilutil import imread
from pylab import subplot, imshow, title, show, gray, cm, figure
from numpy import *

# 'flatten' creates a 2D array from a JPEG.
img = imread('dc_metro.JPG', flatten=True) 

avg_img =(img[1:-1,1:-1]+img[:-2,1:-1]+img[2:,1:-1]+img[1:-1,:-2]+img[1:-1,2:]) / 5.0

figure()
gray()
subplot(1,3,1)
imshow(img)
title('original')
subplot(1,3,2)
imshow(avg_img)
title('1st')
subplot(1,3,3)
imshow(img[1:-1,1:-1] - avg_img)
title('difference')  
show()  


figure()
subplot(1,2,1)
imshow(img)
title('original')
for num in range(50):
    avg_img =(img[1:-1,1:-1]+img[:-2,1:-1]+img[2:,1:-1]+img[1:-1,:-2]+img[1:-1,2:]) / 5.0
    img = avg_img
subplot(1,2,2)
imshow(avg_img)
title('smoothed 50 times')
show()