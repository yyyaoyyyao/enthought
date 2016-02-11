""" 
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

See calc_integral for a bit more advanced example.

See :ref:`calc-derivative-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from pylab import plot, show, subplot, legend, title

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)

dx = x[1:]-x[:-1]
dy = y[1:]-y[:-1]
s = dy/dx

medium = (x[1:]+x[:-1])/2
plot(medium, s,'r+', medium, cos(medium),'b')


show()

