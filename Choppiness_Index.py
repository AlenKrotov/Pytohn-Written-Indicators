import pandas as pd
import numpy as np

def calculate_choppiness_index(high, low, close, period=14):
    """
    Calculate the Choppiness Index.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    period (int): The period over which to calculate the Choppiness Index.

    Returns:
    pd.Series: A Series containing the Choppiness Index values.
    """
    atr = calculate_atr(high, low, close, period)
    high_low_range = high.rolling(period).max() - low.rolling(period).min()
    choppiness = 100 * np.log10(atr.rolling(period).sum() / high_low_range) / np.log10(period)
    return choppiness

# Example usage:
# choppiness = calculate_choppiness_index(high_prices, low_prices, close_prices)
