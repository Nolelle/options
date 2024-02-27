import math
from scipy.stats import norm

# S: Current stock price
# K: Strike price
# T: Time to expiration (in years)
# r: Risk-free interest rate
# σ: Implied volatility
# N(x): Cumulative standard normal distribution function
# e: Mathematical constant (approximately 2.718)

# d1 = [ ln(S/K) + (r + 0.5 * σ^2) * T ] / (σ * √T)
# d2 = d1 - σ * √T

# Call Option Price
# C = S * N(d1) - K * e^(-rT) * N(d2)

# Put Option Price
# P = K * e^(-rT) * N(-d2) - S * N(-d1)


def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))


def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)


def bsm_call_value(S, K, T, r, sigma):
    N_d1 = norm.cdf(d1(S, K, T, r, sigma))
    N_d2 = norm.cdf(d2(S, K, T, r, sigma))
    fair_value = S * N_d1 - K * math.exp(-r * T) * N_d2
    return fair_value


def bsm_put_value(S, K, T, r, sigma):
    N_d1 = norm.cdf(-d1(S, K, T, r, sigma))
    N_d2 = norm.cdf(-d2(S, K, T, r, sigma))
    return K * math.exp(-r * T) * N_d2 - S * N_d1
