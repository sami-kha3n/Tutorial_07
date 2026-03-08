# Author: L. van Veen, Ontario Tech U, 2026
# Starter code for tutorial 7.
import numpy as np
import matplotlib.pyplot as plt
from poly_int import poly_int

# Test functions:
def f(x):                   
    return 1.0/(1.0+x**2)
def g(x):
    return np.exp(-x/10.0)

# Domain:
l = -10.0
r = 10.0
# Grid for plotting and estimating the error.
n_plot = ...
x_out = np.linspace( ... ) 

# Remember errors for an increasing number of nodes for plotting:
err = []
# Loop over increasing number of grid points:
for n in range( ... ):
    fig, axs = plt.subplots( ... )
    N = 2**n
    # x-values for interpolation:
    x = np.linspace( ... )
    # Corresponding y-values:
    y = f(x)
    z = g(x)
    # Compute the interpolant on the fine grid using our code:
    y_out = poly_int( ... )
    z_out = poly_int( ... )
    plt.show()
    axs[0].plot(x_out, ... ,'-k',x_out, ... ,'-r')
    axs[1].plot(x_out, ... ,'-k',x_out, ...,'-r')
    axs[0].set_ylim([f(l)-1.0,f(r)+1.0])
    axs[1].set_ylim([g(l)-1.0,g(r)+1.0])
    axs[0].set_xlabel('x')
    axs[1].set_xlabel('x')
    axs[0].set_ylabel('f and interpolant')
    axs[1].set_ylabel('g and interpolant')
    axs[0].set_title('%d equidistant nodes' % (N))
    plt.show()
    fig, axs = plt.subplots( ... )
    ef = np.absolute( ... )
    eg = np.absolute( ... )
    err.append([N,max(ef),max(eg)])
    axs[0].plot( ... ,'-r')
    axs[0].plot( ... ,'-r')
    axs[0].set_xlabel('x')
    axs[1].set_xlabel('x')
    axs[0].set_ylabel('interpolation error for f')
    axs[1].set_ylabel('interpolation error for g')
    axs[0].set_title('%d equidistant nodes' % (N))
    plt.show()

# Plot the error of interpolation versus the number of nodes:
err = np.asarray(err)
plt.loglog(err[:,0],err[:,1],'-*r')
plt.loglog(err[:,0],err[:,2],'-*b')
plt.show()
