import pandas as pd
import numpy as np

def calculate_mass_index(high, low, period=25, ema_period=9):
    """
    Calculate the Mass Index.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    period (int): The period over which to calculate the Mass Index.
    ema_period (int): The period for the EMAs used in the calculation.

    Returns:
    pd.Series: A Series containing the Mass Index values.
    """
    range_hl = high - low
    ema1 = range_hl.ewm(span=ema_period, adjust=False).mean()
    ema2 = ema1.ewm(span=ema_period, adjust=False).mean()
    mass = ema1 / ema2
    mass_index = mass.rolling(window=period).sum()
    return mass_index

# Example usage:
# mass_index = calculate_mass_index(high_prices, low_prices)
