import pandas as pd
import numpy as np

def calculate_vortex_indicator(high, low, close, period=14):
    """
    Calculate the Vortex Indicator (VI).
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the VI calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing VI+ and VI- values.
    """
    
    tr = pd.DataFrame(index=high.index)
    tr['h-l'] = high - low
    tr['h-pc'] = abs(high - close.shift(1))
    tr['l-pc'] = abs(low - close.shift(1))
    tr['tr'] = tr[['h-l', 'h-pc', 'l-pc']].max(axis=1)
    
    vm_plus = abs(high - low.shift(1))
    vm_minus = abs(low - high.shift(1))
    
    vi_plus = vm_plus.rolling(period).sum() / tr['tr'].rolling(period).sum()
    vi_minus = vm_minus.rolling(period).sum() / tr['tr'].rolling(period).sum()
    
    return pd.DataFrame({
        'VI+': vi_plus,
        'VI-': vi_minus
    })

# Example usage:
# vi_results = calculate_vortex_indicator(high_prices, low_prices, close_prices)
# print(vi_results)
