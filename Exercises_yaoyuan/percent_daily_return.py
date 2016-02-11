""" Percent Daily Return Exercise

In this exercise, you are given the stock values for several consecutive days 
for acme corporation. Your job is to calculate the "percent daily return" for 
each day. The percent daily return is the percentage that the stock changes 
each compared to the day before.

Below you are given the stock prices (there are only 4 days in this example). 
Use slicing a numeric operations to calculate the percent daily return 
(no for loops!). Refer back to the video lecture for inspiration.
"""

from numpy import array

acme = array([10, 11.5, 11, 10, 12])

pdr = (acme[1:]-acme[:-1])/acme[:-1]
print (pdr)