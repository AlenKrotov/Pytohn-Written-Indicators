import pandas as pd
import numpy as np

def calculate_williams_r(high, low, close, period=14):
    """
    Calculate Williams %R indicator.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    period (int): The period over which to calculate Williams %R.

    Returns:
    pd.Series: A Series containing the Williams %R values.
    """
    # Calculate highest high and lowest low
    highest_high = high.rolling(window=period).max()
    lowest_low = low.rolling(window=period).min()

    # Calculate Williams %R
    wr = (highest_high - close) / (highest_high - lowest_low) * -100

    return wr
