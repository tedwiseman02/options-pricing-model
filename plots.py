import numpy as np
import matplotlib.pyplot as plt
from black_scholes import call_price, put_price
from greeks import call_delta, put_delta, gamma, vega


def plot_option_prices(K, T, r, sigma):
    stock_prices = np.linspace(50, 150, 200)

    call_prices = [call_price(S, K, T, r, sigma) for S in stock_prices]
    put_prices = [put_price(S, K, T, r, sigma) for S in stock_prices]

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, call_prices, label="Call Price")
    plt.plot(stock_prices, put_prices, label="Put Price")
    plt.xlabel("Stock Price")
    plt.ylabel("Option Price")
    plt.title("Option Price vs Stock Price")
    plt.legend()
    plt.grid(True)

    plt.savefig("option_prices.png")
    plt.close()

    print("Graph saved as option_prices.png")


def plot_greeks(K, T, r, sigma):
    stock_prices = np.linspace(50, 150, 200)

    call_deltas = [call_delta(S, K, T, r, sigma) for S in stock_prices]
    put_deltas = [put_delta(S, K, T, r, sigma) for S in stock_prices]
    gammas = [gamma(S, K, T, r, sigma) for S in stock_prices]
    vegas = [vega(S, K, T, r, sigma) for S in stock_prices]

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, call_deltas, label="Call Delta")
    plt.plot(stock_prices, put_deltas, label="Put Delta")
    plt.plot(stock_prices, gammas, label="Gamma")
    plt.plot(stock_prices, vegas, label="Vega")
    plt.xlabel("Stock Price")
    plt.ylabel("Greek Value")
    plt.title("Greeks vs Stock Price")
    plt.legend()
    plt.grid(True)

    plt.savefig("greeks.png")
    plt.close()

    print("Graph saved as greeks.png")


def plot_volatility_sensitivity(S, K, r):
    volatilities = np.linspace(0.05, 0.60, 200)

    T_values = [0.25, 0.5, 1.0]  # short, medium, long maturity

    plt.figure(figsize=(10, 6))

    for T in T_values:
        call_prices = [call_price(S, K, T, r, vol) for vol in volatilities]
        plt.plot(volatilities, call_prices, label=f"Call (T={T} yrs)")

    plt.xlabel("Volatility")
    plt.ylabel("Option Price")
    plt.title("Call Option Price vs Volatility (Different Maturities)")
    plt.legend()
    plt.grid(True)

    plt.savefig("volatility_sensitivity.png")
    plt.close()

    print("Graph saved as volatility_sensitivity.png")