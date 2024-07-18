import pandas as pd
import numpy as np

def calculate_mfi(high, low, close, volume, period=14):
    """
    Calculate the Money Flow Index (MFI).
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    volume (pd.Series): Volume for the period.
    period (int): The number of periods to use for the MFI calculation.
    
    Returns:
    pd.Series: A Series containing MFI values.
    """
    
    typical_price = (high + low + close) / 3
    raw_money_flow = typical_price * volume
    
    positive_flow = pd.Series(np.where(typical_price > typical_price.shift(1), raw_money_flow, 0), index=typical_price.index)
    negative_flow = pd.Series(np.where(typical_price < typical_price.shift(1), raw_money_flow, 0), index=typical_price.index)
    
    positive_mf = positive_flow.rolling(window=period).sum()
    negative_mf = negative_flow.rolling(window=period).sum()
    
    mfi = 100 - (100 / (1 + positive_mf / negative_mf))
    
    return pd.Series(mfi, name='MFI')

# Example usage:
# mfi_results = calculate_mfi(high_prices, low_prices, close_prices, volume)
# print(mfi_results)
