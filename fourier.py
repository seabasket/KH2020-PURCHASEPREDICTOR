import numpy as np
from numpy import newaxis
from scipy.integrate import simps

TAU = 2 * np.pi
PI2 = np.pi / 2


# ----- CAT Fourier Analysis ------


def cat_coeff(x, k, s):
    # Number of samples for integration
    t = np.linspace(0, TAU, s, endpoint=False)

    # Approximate Data Transform using Simpson's Rule
    rho = 1j * PI2 * np.floor((t[:, newaxis] @ k[newaxis, :]) / PI2)
    A = simps(np.einsum("tj,tk->tjk", np.exp(-rho), np.exp(rho)), t, axis=0) / TAU
    B = simps(np.einsum("t,tj->tj", x(t), np.exp(-rho)), t, axis=0) / TAU

    # Compute coefficients in Frequency Domain
    return np.linalg.solve(A, B)


def phi(k, t):
    # Extend step function periodically
    t = np.mod(t, TAU)
    return np.exp(1j * PI2 * np.floor((t[:, newaxis] @ k[newaxis, :]) / PI2))


def analyze(x, k=23, s=1999):
    # Compute coefficients of 2k+1 terms in CAT Sequence
    k = np.arange(-k, k + 1)
    Yk = cat_coeff(x, k, s)

    # Predict category for any given time t
    return lambda t: np.real(np.einsum("tk,k->t", phi(k, t), Yk))


# ----- I/O Formatting ------


def interpolate(arr):
    # Convert discrete time series to a stepwise function
    return lambda t: arr[np.floor(len(arr) * np.mod(t, TAU) / TAU).astype(int)]


def interpret(qcat):
    # Simplify into an unambiguous category prediction
    return np.clip(np.around(qcat), 0, None).astype(int)


# ---- DEBUG -----


if __name__ == "__main__":
    interval = 30
    x = np.array([1 if _ % 10 == 0 else 0 for _ in range(interval)])

    x = interpolate(x)
    xp = analyze(x, 20, 9999)
    t = np.linspace(0, 2 * TAU, 2 * interval, endpoint=False)

    print(f"Quasi-Category: {xp(t)}\n")
    print(f"Predicted: {interpret(xp(t))}\n")
    print(f"Actual: {x(t)}\n")
