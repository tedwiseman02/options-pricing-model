# Options Pricing & Risk Analysis

This project implements the Black-Scholes model in Python to price European call and put options and calculate key option Greeks. It also includes visualisations showing how option values and sensitivities change with stock price and volatility.

## Project Overview

The aim of this project is to demonstrate practical understanding of derivative pricing, risk sensitivities, and financial modelling using Python.

The model calculates:
- European call option price
- European put option price
- Delta
- Gamma
- Vega
- Theta
- Rho

The project also generates charts to visualise:
- option price vs stock price
- Greeks vs stock price
- call option price vs volatility for different maturities

## Files in This Project

- `main.py` – runs the full model and generates outputs  
- `black_scholes.py` – contains Black-Scholes pricing functions  
- `greeks.py` – contains functions for calculating Greeks  
- `plots.py` – generates and saves visualisations  
- `option_prices.png` – option price sensitivity chart  
- `greeks.png` – Greeks sensitivity chart  
- `volatility_sensitivity.png` – volatility sensitivity chart  

## Inputs

The model uses the following inputs:

- `S` = stock price  
- `K` = strike price  
- `T` = time to maturity in years  
- `r` = risk-free interest rate  
- `sigma` = volatility  

## Example Values

```python
S = 100
K = 105
T = 0.5
r = 0.05
sigma = 0.20
