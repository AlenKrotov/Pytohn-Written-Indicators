import pandas as pd
import numpy as np

def calculate_donchian_channel(high, low, period=20):
    """
    Calculate the Donchian Channel.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    period (int): The number of periods to use for the channel calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing Upper, Middle, and Lower Donchian Channel values.
    """
    
    upper = high.rolling(window=period).max()
    lower = low.rolling(window=period).min()
    middle = (upper + lower) / 2
    
    return pd.DataFrame({
        'Upper': upper,
        'Middle': middle,
        'Lower': lower
    })

# Example usage:
# donchian_results = calculate_donchian_channel(high_prices, low_prices)
# print(donchian_results)
