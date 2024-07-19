import pandas as pd
import numpy as np

def calculate_volume_weighted_average_price(high, low, close, volume):
    """
    Calculate the Volume Weighted Average Price (VWAP).

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    volume (pd.Series): Series of volume data.

    Returns:
    pd.Series: A Series containing the VWAP values.
    """
    typical_price = (high + low + close) / 3
    vwap = (typical_price * volume).cumsum() / volume.cumsum()
    return vwap

# Example usage:
# vwap = calculate_volume_weighted_average_price(high_prices, low_prices, close_prices, volume)
