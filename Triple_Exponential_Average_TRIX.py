import pandas as pd
import numpy as np

def calculate_trix(close, period=15):
    """
    Calculate the Triple Exponential Average (TRIX) indicator.

    Parameters:
    close (pd.Series): Series of closing prices.
    period (int): The period for the EMA calculations.

    Returns:
    pd.Series: A Series containing the TRIX values.
    """
    # Calculate first EMA
    ema1 = close.ewm(span=period, adjust=False).mean()

    # Calculate second EMA
    ema2 = ema1.ewm(span=period, adjust=False).mean()

    # Calculate third EMA
    ema3 = ema2.ewm(span=period, adjust=False).mean()

    # Calculate TRIX
    trix = (ema3 - ema3.shift(1)) / ema3.shift(1) * 100

    return trix

# Example usage:
# trix_values = calculate_trix(close_prices)
