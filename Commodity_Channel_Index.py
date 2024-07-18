import pandas as pd
import numpy as np

def calculate_cci(high, low, close, period=20):
    """
    Calculate the Commodity Channel Index (CCI).
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the CCI calculation.
    
    Returns:
    pd.Series: A Series containing CCI values.
    """
    
    typical_price = (high + low + close) / 3
    sma = typical_price.rolling(window=period).mean()
    mad = typical_price.rolling(window=period).apply(lambda x: np.abs(x - x.mean()).mean())
    
    cci = (typical_price - sma) / (0.015 * mad)
    
    return pd.Series(cci, name='CCI')

# Example usage:
# cci_results = calculate_cci(high_prices, low_prices, close_prices)
# print(cci_results)
