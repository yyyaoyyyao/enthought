
# Volatility Estimation
# =====================
# 
# A standard model of stock price fluctuation is:
# 
# $$\frac{dS}{S} = \mu dt + \sigma \epsilon \sqrt{\strut dt}$$
# 
# where:
#     
# * $S$ is the stock price.
# * $dS$ is the change in stock price.
# * $\mu$ is the rate of return.
# * $dt$ is the time interval.
# * $\epsilon$ is a normal random variable with mean 0 and variance 1 that is
#   uncorrelated with other time intervals.
# * $\sigma$ is the volatility.
# 
# It is desired to make estimates of $\sigma$ from historical price information.
# There are simple approaches to do this that assume volatility is constant over a
# period of time. It is more accurate, however, to recognize that $\sigma$ changes
# with each day and therefore should be estimated at each day. To effectively do
# this from historical price data alone, some kind of model is needed.
# 
# The GARCH(1,1) model for volatility at time *n*, estimated from data
# available at the end of time $n-1$ is:
# 
# $$\sigma_n^2 = \gamma V_L + \alpha u_{n-1}^2 + \beta \sigma_{n-1}^2$$
# 
# where:
# 
# * $V_L$ is long-running volatility
# * $\alpha+\beta+\gamma = 1$
# * $u_n = log(S_n / S_{n-1})$ or $(S_n - S_{n-1})/S_{n-1}$
# 
# Estimating $V_L$ can be done as the mean of $u_n^2$ (variance of $u_n$).
# Estimating parameters $\alpha$ and $\beta$ is done by finding the parameters that
# maximize the likelihood that the data $u_n$ would be observed. If it is assumed
# that the $u_n$ are normally distributed with mean 0 and variance $\sigma_n$, this
# is equivalent to finding $\alpha$ and $\beta$ that minimize:
# 
# $$L(\alpha, \beta) = \sum_{n}(log(\sigma_n^2) + u_n^2 / \sigma_n^2)$$
# 
# where $\sigma_n^2$ is computed as above. 

# Question 1
# ----------
# 
# Create a function to read in daily data from `sp500hst.txt` for the S&P 500 for a particular stock. The file format is:
# 
#        date, symbol, open, high, low, close, volume


import numpy as np
TRADING_DAYS = 252
filename = "sp500hst.txt"



# your code goes here
format = [('date', int), ('symbol', 'S4'), ('open', float),
       ('high', float), ('low', float), ('close', float),
       ('volume', int)]

def read_data(filename):
   
    data = np.genfromtxt(filename, delimiter=",", dtype=format)
    return data

def read_symbol(filename, symbol):
    
    data = read_data(filename)
    return data[data['symbol']==symbol]

# Question 2
# ----------
# 
# Create a function to estimate volatility per annum for a specific number of periods (assume 252 trading days in a year).


# your code goes here
def volatility(S, periods=4, repeat=False):
   
    N = len(S)
    div = N // periods
    S = S[:periods * div]
    # place each quarter on its own row
    S = S.reshape(periods, -1)
    # Compute u
    u = np.log(S[:, 1:] / S[:, :-1])
    # Estimate volatility per annum
    #   by adjusting daily volatility calculation
    sigma = np.sqrt(u.var(axis=-1) * TRADING_DAYS)
    if repeat:
        sigma = sigma.repeat(S.shape[-1])
    return sigma[1:]

# Question 3
# ----------
# 
# Create a function to compute $\sigma^2_n$ for each $n$ from $\alpha$ and $\beta$ and $u_n^2$ (you may need to use a for loop for this).  Use $V_L$ to start the recursion.


# your code goes here
def sigmasq_g(usq, alpha, beta):
    """sigma_n**2 assuming the GARCH(1,1) model of::

        sigma_n**2 = gamma*VL + alpha*sigma_n**2 + beta*u_n**2

    where gamma + alpha + beta = 1
    and  VL = mean(usq)
    """
    sigmasq = np.empty_like(usq)
    VL = usq.mean()
    sigmasq[0] = VL
    omega = VL * (1 - alpha - beta)
    for i in range(1, len(usq)):
        sigmasq[i] = omega + alpha * sigmasq[i - 1] + beta * usq[i - 1]
    return sigmasq


# Question 4
# ----------
# 
# Create a function that will estimate volatility using GARCH(1,1) approach by minimizing ``L(alpha, beta)``.


from scipy.optimize import fmin



# your code goes here
def _minfunc(x, usq):
    alpha, beta = x
    sigsq = sigmasq_g(usq, alpha, beta)
    return (np.log(sigsq) + usq / sigsq).sum()

def garch_volatility(S):
    """Volatility per annum for each day computed from historical
    close price information using the GARCH(1,1) and maximum
    likelihood estimation of the parameters.
    """
    x0 = [0.5, 0.5]
    usq = np.log(S[1:]/S[:-1])**2
    xopt = fmin(_minfunc, x0, args=(usq,))
    sigmasq = sigmasq_g(usq, *xopt)
    print "alpha = ", xopt[0]
    print "beta = ", xopt[1]
    print "V_L = ", usq.mean()
    return np.sqrt(sigmasq*TRADING_DAYS)

# Question 5
# ----------
# 
# Use the functions to construct a plot of volatility per annum for a stock of your choice (use 'AAPL' if you don't have a preference) using quarterly, monthly, and GARCH(1,1) estimates.


from matplotlib.pyplot import plot, title, xlabel, ylabel, legend, show



# your code goes here
stock = 'MSFT'
data = read_symbol('sp500hst.txt', stock)
S = data['close']
sig_4 = volatility(S, 4, repeat=True)
sig_12 = volatility(S, 12, repeat=True)
sig_g = garch_volatility(S)

plot(sig_g, label='GARCH(1,1)')
plot(sig_12, label='Monthly average')
plot(sig_4, label='Quarterly average')

title('Volatility estimates')
xlabel('trading day')
ylabel('volatility per annum')
legend(loc='lower right')
show()