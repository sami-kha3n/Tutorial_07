# Starter code for tutorial 7 (fixed)
import numpy as np
import matplotlib.pyplot as plt
from poly_int import poly_int

# Test functions:
def f(x):
    return 1.0 / (1.0 + x**2)

def g(x):
    return np.exp(-x/10.0)

# Domain:
l = -10.0
r = 10.0
# Grid for plotting and estimating the error.
n_plot = 2000
x_out = np.linspace(l, r, n_plot)

# Remember errors for an increasing number of nodes for plotting:
err = []
# Loop over N = 4, 8, 16, 32
for exp in range(2, 6):  # 2->4, 3->8, 4->16, 5->32
    N = 2**exp
    # x-values for interpolation (equidistant)
    x = np.linspace(l, r, N)
    y = f(x)
    z = g(x)
    y_out = poly_int(x, y, x_out)
    z_out = poly_int(x, z, x_out)

    # Plot functions and interpolants
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    axs[0].plot(x_out, f(x_out), '-k', label='f (true)')
    axs[0].plot(x_out, y_out, '-r', label='PN (interp)')
    axs[1].plot(x_out, g(x_out), '-k', label='g (true)')
    axs[1].plot(x_out, z_out, '-r', label='QN (interp)')
    axs[0].set_ylim([min(f(x_out)) - 1.0, max(f(x_out)) + 1.0])
    axs[1].set_ylim([min(g(x_out)) - 1.0, max(g(x_out)) + 1.0])
    axs[0].set_xlabel('x')
    axs[1].set_xlabel('x')
    axs[0].set_ylabel('f and interpolant')
    axs[1].set_ylabel('g and interpolant')
    axs[0].set_title('%d equidistant nodes' % (N))
    axs[0].legend()
    axs[1].legend()
    plt.tight_layout()
    plt.show()

    # Plot errors
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    ef = np.abs(f(x_out) - y_out)
    eg = np.abs(g(x_out) - z_out)
    err.append([N, np.max(ef), np.max(eg)])
    axs[0].plot(x_out, ef, '-r')
    axs[1].plot(x_out, eg, '-r')
    axs[0].set_xlabel('x')
    axs[1].set_xlabel('x')
    axs[0].set_ylabel('interpolation error for f')
    axs[1].set_ylabel('interpolation error for g')
    axs[0].set_title('%d equidistant nodes' % (N))
    plt.tight_layout()
    plt.show()

# Plot the error of interpolation versus the number of nodes:
err = np.asarray(err)
plt.loglog(err[:, 0], err[:, 1], '-*r', label='f max error')
plt.loglog(err[:, 0], err[:, 2], '-*b', label='g max error')
plt.xlabel('Number of nodes (N)')
plt.ylabel('Maximum interpolation error')
plt.legend()
plt.grid(True, which='both', ls='--')
plt.show()
