""" 
Load Array from Text File
-------------------------

0. From the IPython prompt, type::

        In [1]: loadtxt?
   
   to see the options on how to use the loadtxt command.
    

1. Use loadtxt to load in a 2D array of floating point values from
   'float_data.txt'.  The data in the file looks like::
   
        1 2 3 4 
        5 6 7 8
   
   The resulting data should be a 2x4 array of floating point values.

2. In the second example, the file 'float_data_with_header.txt' has 
   strings as column names in the first row::
   
        c1 c2 c3 c4
         1  2  3  4
         5  6  7  8
   
   Ignore these column names, and read the remainder of the data into
   a 2D array.  
   
   Later on, we'll learn how to create a "structured array" using 
   these column names to create fields within an array.

Bonus
~~~~~

3. A third example is more involved. It contains comments in multiple
   locations, uses multiple formats, and includes a useless column to
   skip::

    -- THIS IS THE BEGINNING OF THE FILE --
    
    % This is a more complex file to read!

    % Day,  Month,  Year, Useless Col, Avg Power
       01,     01,  2000,      ad766,         30 
       02,     01,  2000,       t873,         41
    % we don't have Jan 03rd!
       04,     01,  2000,       r441,         55
       05,     01,  2000,       s345,         78
       06,     01,  2000,       x273,        134 % that day was crazy
       07,     01,  2000,       x355,         42

    %-- THIS IS THE END OF THE FILE --

4. Last year your summer intern developed a FORTRAN program which wrote three
   columns of data (x, volts, and pres) to a text file.  You have just run it again,
   but with parameter values very different from what you used last time.
   You find that the output, readings.out, contains these lines::

       5.000 80.103  4.003
      15.000 84.544  1.984
      25.000 95.041  2.887
      35.000 99.522  4.095
      45.000107.543  5.163
      55.000113.834  6.554
      65.000117.543  8.234
      75.000121.077 11.400
      85.000120.813 13.481
      95.000119.549 15.333
     105.000117.435 16.501

   There are supposed to be three columns, but the values in the middle
   column are bigger than before, and now there is no space between the first
   and second columns after the first four rows.

   genfromtxt() can deal with this; read the docstring, paying special
   attention to the 'delimiter' argument.

   Use genfromtxt() to read this file, and use matplotlib with subplot to
   make two plots, x vs. volts and x vs. pres, in a single plot figure.
"""

from numpy import loadtxt
# for bonus (part 4)
from numpy import genfromtxt
from matplotlib.pyplot import subplot, plot, xlabel, ylabel, title, grid, show

print("Q1")
array1 = loadtxt('float_data.txt')
print(array1)

print("Q2")
array2 = loadtxt('float_data_with_header.txt',skiprows = 1)
print(array2)

print("Q3")
array3 = loadtxt('complex_data_file.txt',skiprows = 1,dtype = int, delimiter = ",", usecols = (0,1,2,4), comments = "%")
print(array3)

print "Q4"
data = genfromtxt('readings.out', delimiter=(7,7,7))
subplot(2, 1, 1)
plot(data[:,0], data[:,1])
ylabel('volts')
grid(True)
subplot(2, 1, 2)
plot(data[:,0], data[:,2])
ylabel('pres')
xlabel('x')
grid(True)
show()