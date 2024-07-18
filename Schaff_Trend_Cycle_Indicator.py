import pandas as pd
import numpy as np

def calculate_stc(close, fast_period=23, slow_period=50, stc_period=10):
    """
    Calculate the Schaff Trend Cycle (STC).
    
    Parameters:
    close (pd.Series): Closing prices for the period.
    fast_period (int): The number of periods for the fast MACD line.
    slow_period (int): The number of periods for the slow MACD line.
    stc_period (int): The number of periods for the STC calculation.
    
    Returns:
    pd.Series: A Series containing STC values.
    """
    
    ema_fast = close.ewm(span=fast_period, adjust=False).mean()
    ema_slow = close.ewm(span=slow_period, adjust=False).mean()
    macd = ema_fast - ema_slow
    
    def stc_formula(x):
        lowest_low = x.min()
        highest_high = x.max()
        return 100 * ((x[-1] - lowest_low) / (highest_high - lowest_low))
    
    stc = macd.rolling(window=stc_period).apply(stc_formula)
    stc = stc.rolling(window=3).mean()  # Further smoothing
    
    return pd.Series(stc, name='STC')

# Example usage:
# stc_results = calculate_stc(close_prices)
# print(stc_results)
