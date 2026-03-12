import numpy as np

def forwardSub(L, y):
    """
    Solve the lower-triangular system L z = y using forward substitution.
    Returns a 1-D numpy array of length n.
    """
    L = np.asarray(L, dtype=float)
    y = np.reshape(np.asarray(y, dtype=float), (-1,))
    n = L.shape[0]
    z = np.zeros(n, dtype=float)
    for i in range(n):
        s = y[i]
        for j in range(i):
            s -= L[i, j] * z[j]
        z[i] = s / L[i, i]
    return z

def phi(x, xs, k):
    """
    Newton basis product phi_k(x) = prod_{i=0}^{k-1} (x - xs[i]).
    k=0 -> 1
    """
    q = 1.0
    for i in range(k):
        q *= (x - xs[i])
    return q

def poly_int(xs, ys, xout):
    """
    Newton-form interpolation:
    xs, ys : 1D arrays of length N
    xout   : 1D array of points to evaluate
    Returns yout : 1D array of same length as xout.
    """
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    xout = np.asarray(xout, dtype=float)

    n = xs.size - 1
    V = np.zeros((n+1, n+1), dtype=float)
    for i in range(n+1):
        for j in range(i+1):
            V[i, j] = phi(xs[i], xs, j)

    a = forwardSub(V, ys)  # a is 1-D array of Newton coeffs

    m = xout.size
    yout = np.zeros(m, dtype=float)
    for i in range(m):
        val = 0.0
        for j in range(n+1):
            val += a[j] * phi(xout[i], xs, j)
        yout[i] = val

    return yout
