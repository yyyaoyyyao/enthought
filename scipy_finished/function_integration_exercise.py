
# Function integration
# ====================
# 
# This is an exercise to try out the numerical integration routines in SciPy, which we can compare to some analytic results, to see how well the numerical integration performs.

# Question 1
# ----------
# 
# Use `scipy.integrate.quad` to integrate sin from 0 to $\dfrac{\pi}{2}$ and print out the result.

# Hint: Look at the docstring for quad with
# `>>> quad?`

from pylab import *
from numpy import pi, sin
from scipy.integrate import quad



# your code goes here
result, error = quad(sin,0, pi/2)
print "integral(sin 0->pi/2) = {}".format(result)

# Question 2
# ----------
# 
# Integrate sin from 0 to x where x is a range of values from 0 to $2\pi$. Compare this to the exact solution, -cos(x) + cos(0), on a plot. Also plot the error between the two.

# Hint: Use `vectorize` so that `integrate.quad` works with arrays as inputs and produces arrays as outputs.


from numpy import linspace, vectorize, cos
from matplotlib.pyplot import plot, legend, show, subplot, xlabel, ylabel, title

x = linspace(0, 2*pi, 101)



# your code goes here



vquad = vectorize(quad)

 
approx, error_est = vquad(sin, 0, x)


exact = -cos(x) + cos(0)


subplot(1,2,1)
plot(x, approx, 'r+',label="Approx")
plot(x, exact, label="Exact")
xlabel('x')
ylabel('integral(sin)')
title('Integral of sin from 0 to x')
legend()

subplot(1,2,2)
plot(x, exact-approx)
title('Error in approximation')
show()