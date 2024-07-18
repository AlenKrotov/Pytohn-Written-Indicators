import pandas as pd
import numpy as np

def calculate_cmf(high_prices, low_prices, close_prices, volume, period=20):
    """
    Calculate the Chaikin Money Flow (CMF).
    
    Parameters:
    high_prices (pd.Series): High prices for the period.
    low_prices (pd.Series): Low prices for the period.
    close_prices (pd.Series): Closing prices for the period.
    volume (pd.Series): Volume for the period.
    period (int): The number of periods to use for the CMF calculation.
    
    Returns:
    pd.Series: A Series containing CMF values.
    """
    
    mfm = ((close_prices - low_prices) - (high_prices - close_prices)) / (high_prices - low_prices)
    mfv = mfm * volume
    
    cmf = mfv.rolling(window=period).sum() / volume.rolling(window=period).sum()
    
    return pd.Series(cmf, name='CMF')

# Example usage:
# cmf_results = calculate_cmf(high_prices, low_prices, close_prices, volume)
# print(cmf_results)
