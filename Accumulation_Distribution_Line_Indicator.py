import pandas as pd
import numpy as np

def calculate_adl(high, low, close, volume):
    """
    Calculate the Accumulation/Distribution Line (ADL).
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    volume (pd.Series): Volume for the period.
    
    Returns:
    pd.Series: A Series containing ADL values.
    """
    
    clv = ((close - low) - (high - close)) / (high - low)
    clv = clv.fillna(0)  # Handle potential division by zero
    
    adl = (clv * volume).cumsum()
    
    return pd.Series(adl, name='ADL')

# Example usage:
# adl_results = calculate_adl(high_prices, low_prices, close_prices, volume)
# print(adl_results)
