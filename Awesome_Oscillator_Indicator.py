import pandas as pd
import numpy as np

def calculate_awesome_oscillator(high, low, short_period=5, long_period=34):
    """
    Calculate the Awesome Oscillator.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    short_period (int): The number of periods for the short-term SMA.
    long_period (int): The number of periods for the long-term SMA.
    
    Returns:
    pd.Series: A Series containing Awesome Oscillator values.
    """
    
    median_price = (high + low) / 2
    
    ao = (median_price.rolling(window=short_period).mean() - 
          median_price.rolling(window=long_period).mean())
    
    return pd.Series(ao, name='AO')

# Example usage:
# ao_results = calculate_awesome_oscillator(high_prices, low_prices)
# print(ao_results)
