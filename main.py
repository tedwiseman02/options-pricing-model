from plots import plot_option_prices, plot_greeks, plot_volatility_sensitivity
from black_scholes import call_price, put_price
from greeks import (
    call_delta, put_delta, gamma, vega,
    call_theta, put_theta, call_rho, put_rho
)

S = 100
K = 105
T = 0.5
r = 0.05
sigma = 0.20

print("OPTION PRICES")
print("Call:", round(call_price(S, K, T, r, sigma), 2))
print("Put:", round(put_price(S, K, T, r, sigma), 2))

print("\nGREEKS")
print("Call Delta:", round(call_delta(S, K, T, r, sigma), 4))
print("Put Delta:", round(put_delta(S, K, T, r, sigma), 4))
print("Gamma:", round(gamma(S, K, T, r, sigma), 4))
print("Vega:", round(vega(S, K, T, r, sigma), 4))
print("Call Theta:", round(call_theta(S, K, T, r, sigma), 4))
print("Put Theta:", round(put_theta(S, K, T, r, sigma), 4))
print("Call Rho:", round(call_rho(S, K, T, r, sigma), 4))
print("Put Rho:", round(put_rho(S, K, T, r, sigma), 4))
plot_option_prices(K, T, r, sigma)
plot_greeks(K, T, r, sigma)
plot_volatility_sensitivity(S, K, r)