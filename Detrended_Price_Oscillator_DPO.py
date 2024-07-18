import pandas as pd
import numpy as np

def calculate_dpo(close, period=20):
    """
    Calculate the Detrended Price Oscillator (DPO).
    
    Parameters:
    close (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the DPO calculation.
    
    Returns:
    pd.Series: A Series containing DPO values.
    """
    
    shift = period // 2 + 1
    ma = close.rolling(window=period).mean().shift(shift)
    dpo = close - ma
    
    return pd.Series(dpo, name='DPO')

# Example usage:
# dpo_results = calculate_dpo(close_prices)
# print(dpo_results)
