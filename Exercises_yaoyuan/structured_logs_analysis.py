"""
Structured Array
----------------

In this exercise you will read columns of data into a structured array using 
loadtxt and combine that array to a regular array to analyze the data and learn 
how the pressure velocity evolves as a function of the shear velocity in sound 
waves in the Earth.

1. The data in 'short_logs.crv' has the following format::

       DEPTH          CALI       S-SONIC   ...
       8744.5000   -999.2500   -999.2500   ...
       8745.0000   -999.2500   -999.2500   ...
       8745.5000   -999.2500   -999.2500   ...

   Here the first row defines a set of names for the columns
   of data in the file.  Use these column names to define a 
   dtype for a structured array that will have fields 'DEPTH',
   'CALI', etc.  Assume all the data is of the float64 data
   format.

2. Use the 'loadtxt' method from numpy to read the data from
   the file into a structured array with the dtype created
   in (1).  Name this array 'logs'

3. The 'logs' array is nice for retrieving columns from the data.
   For example, logs['DEPTH'] returns the values from the DEPTH
   column of the data.  For row-based or array-wide operations,
   it is more convenient to have a 2D view into the data, as if it
   is a simple 2D array of float64 values.

   Create a 2D array called 'logs_2d' using the view operation.
   Be sure the 2D array has the same number of columns as in the 
   data file.  

4. -999.25 is a "special" value in this data set.  It is 
   intended to represent missing data.  Replace all of these
   values with NaNs.  Is this easier with the 'logs' array
   or the 'logs_2d' array?

5. Create a mask for all the "complete" rows in the array.
   A complete row is one that doesn't have any NaN values measured
   in that row.

   HINT: The ``all`` function is also useful here.

6. Plot the VP vs VS logs for the "complete" rows.

See :ref:`structured-array-solution`.
"""
from numpy import dtype, loadtxt, float64, NaN, isfinite, all
from matplotlib.pyplot import plot, show, xlabel, ylabel

# Open the file.
log_file = open('short_logs.crv')
    
# The first line is a header that has all the log names.
#1
header = log_file.readline()
log_names = header.split()
logs_dtype_format = zip(log_names, ['f8']*len(log_names))
logs_dtype = dtype(logs_dtype_format)
#logs_dtype = dtype([('DEPTH','f8'),('CALI','f8'),('S-SONIC','f8'),('P-SONIC','f8'),('GR','f8'),('LITH','f8'),('RESISTIVITY','f8'),('NPHI','f8'),('POROS','f8'),('RHOB','f8'),('SWARCH','f8'),('SW_I','f8'),('VP','f8'),('VSH','f8'),('VS','f8')])
#2
logs = loadtxt('short_logs.crv',skiprows=1,dtype = logs_dtype)

#3
logs_2d = logs.view(float64)
logs_2d.shape = [-1,len(log_names)]

#4
logs_2d[logs_2d == -999.25] = NaN

#5
mask = all(isfinite(logs_2d), axis=-1)
complete_logs = logs[mask]

#6
plot(complete_logs['VS'], complete_logs['VP'],'ro')
xlabel('VS')
ylabel('VP')
show()  