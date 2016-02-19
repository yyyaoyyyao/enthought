# -*- coding: cp936 -*-

# Curve Fitting
# =============
# 
# SciPy provides many methods to fit curves to your data points. The fitted curves can be a much cleaner way to represent your data.
# 
# Question 1
# ----------
# Plot the following noisy, sinusoidal data produced for you with a randomized generator.

from pylab import *
import numpy as np
from scipy.stats import norm

def noisy_data(x):
    phase = pi / 4
    frequency = 0.85
    noise = norm.rvs(size=x.shape) * 0.5
    return np.sin(x * frequency + phase) + noise

x = np.linspace(-pi, pi, 100)
y = noisy_data(x)



# your code goes here
figure()
plot(x, y,'.')
show()
# Question 2
# ----------
# 
# Take a look at your data. Could you use a polynomial to fit the data? What order polynomial is appropriate?
# Plot your fit against the original data.
# How good is the fit? Can you make the fit better by increasing the polynomial order?

# Hint: `1 - R ** 2` can be calculated by dividing the sum of the squared model error by the overall variation.


from numpy import polyfit, poly1d

# your code goes here
fit = polyfit(x, y, 3)

fit_func = poly1d(fit)
figure()
plot(x, y, 'b.')
plot(x, fit_func(x), 'r-')
show()

model_sq_err = (y - fit_func(x)) ** 2
std_err = np.sqrt(model_sq_err.mean())


total_sq_err = (y - y.mean()) ** 2
r2 = 1 - model_sq_err.sum() / total_sq_err.sum()

print "std err = {}".format(std_err)
print "r2 = {}".format(r2)




# Question 3
# ----------
# 
# You find out that your data has the form `y=sin(ωx+ϕ)`. Set up a function to fit the data to this form.


# your code goes here
def fit_function(x, a, phi):
    return np.sin(x * a + phi)

# Question 4
# ----------
# 
# Use `curve_fit()` to find the best fit for the frequency and phase shift parameters in the data.


from scipy.optimize import curve_fit



# your code goes here
p_est, err_est = curve_fit(fit_function, x, y, [0, 1])
figure()
plot(x, y, 'b.')
plot(x, fit_function(x, *p_est), 'r-')
title('y = sin({:.3}x + {:.3})'.format(*p_est))
show()
# Standard error is the square root of the average squared distance
# of the data points from the model points
model_sq_err = (y - fit_function(x, *p_est)) ** 2
std_err = np.sqrt(model_sq_err.mean())

# Correlation coefficient (R2) is the amount of variation explained by the model
overall_sq_err = (y - y.mean()) ** 2
r2 = 1 - model_sq_err.sum() / overall_sq_err.sum()

print "std err = {}".format(std_err)
print "r2 = {}".format(r2)

