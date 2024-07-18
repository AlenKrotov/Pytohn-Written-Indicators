import pandas as pd
import numpy as np

def calculate_elder_ray(high, low, close, period=13):
    """
    Calculate the Elder-Ray Index.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the EMA calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing Bull Power and Bear Power values.
    """
    
    ema = close.ewm(span=period, adjust=False).mean()
    bull_power = high - ema
    bear_power = low - ema
    
    return pd.DataFrame({
        'Bull Power': bull_power,
        'Bear Power': bear_power,
        'EMA': ema
    })

# Example usage:
# elder_ray_results = calculate_elder_ray(high_prices, low_prices, close_prices)
# print(elder_ray_results)
