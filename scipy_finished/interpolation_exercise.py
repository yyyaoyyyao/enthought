
# Interpolation
# =============
# 
# In this exercise, we will use some of the SciPy interpolation functions, to clean up some bad data. We will read a datafile, which has some invalid entries, which we will then fill with plausible interpolated results. We will then make a plot of the cleaned data, and as a bonus, will highlight the interpolated regions on the plot.

# Question 1
# ----------
# 
# Read the data in `ud667.csv`. Note that some of the values are -999.25, which is a special value for "Missing data".


from numpy import genfromtxt, empty, NaN

data = genfromtxt('ud667.csv', names=True)


# your code goes here


# Question 2
# ----------
# 
# Use the function `interp1d` in the `scipy.interpolate` module to fill in the "bad" regions (where the data is -999.25) of the VP data with data from the "good" areas in the logs.


from scipy.interpolate import interp1d

vp = data['VP']
depth = data['DEPTH']
bad_data_mask = (vp == -999.25)
good_data_mask = (vp != -999.25)

interp_depth_need = depth [bad_data_mask]

interp = interp1d(depth[good_data_mask], vp[good_data_mask], kind=3, bounds_error=False)

interp_vp = interp(interp_depth_need)


# your code goes here


# Question 3
# ----------
# 
# Create a plot of VP vs. DEPTH using the interpolated data.

from pylab import plot,xlabel,ylabel,title,show,figure

after_interp_vp = vp.copy()
after_interp_vp[bad_data_mask] = interp_vp
figure()
plot(depth, after_interp_vp)

xlabel('depth')

ylabel('vp')

title('Data')

show()
# your code goes here


# Question 4
# ----------
# 
# Bonus: Create another plot of VP vs DEPTH, but change the color
#  of the interpolated part of the data.


# your code goes here
figure()
plot(depth, after_interp_vp, 'b')
after_interp_vp[good_data_mask] = NaN
plot(depth, after_interp_vp, 'r')
show()