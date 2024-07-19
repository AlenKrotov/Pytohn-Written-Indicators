import pandas as pd
import numpy as np

def calculate_ultimate_oscillator(high, low, close, period1=7, period2=14, period3=28):
    """
    Calculate the Ultimate Oscillator.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    period1 (int): The first (shortest) period.
    period2 (int): The second (medium) period.
    period3 (int): The third (longest) period.

    Returns:
    pd.Series: A Series containing the Ultimate Oscillator values.
    """
    # Calculate buying pressure
    bp = close - pd.DataFrame([low, close.shift(1)]).min()

    # Calculate true range
    tr = pd.DataFrame([high - low, 
                       abs(high - close.shift(1)), 
                       abs(low - close.shift(1))]).max()

    # Calculate average true range for each period
    avg1 = bp.rolling(period1).sum() / tr.rolling(period1).sum()
    avg2 = bp.rolling(period2).sum() / tr.rolling(period2).sum()
    avg3 = bp.rolling(period3).sum() / tr.rolling(period3).sum()

    # Calculate Ultimate Oscillator
    uo = 100 * ((4 * avg1) + (2 * avg2) + avg3) / 7

    return uo

# Example usage:
# uo_values = calculate_ultimate_oscillator(high_prices, low_prices, close_prices)
