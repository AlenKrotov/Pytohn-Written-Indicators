import pandas as pd
import numpy as np

def calculate_ehlers_fisher(close, period=10):
    """
    Calculate the Ehlers Fisher Transform.
    
    Parameters:
    close (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing Fisher Transform and its Signal line.
    """
    
    high = close.rolling(window=period).max()
    low = close.rolling(window=period).min()
    
    value = 0.33 * 2 * ((close - low) / (high - low) - 0.5) + 0.67 * value if len(value) > 0 else 0
    value = pd.Series(value, index=close.index)
    value = value.fillna(0)
    
    fisher = 0.5 * np.log((1 + value) / (1 - value))
    fisher = pd.Series(fisher, index=close.index).fillna(0)
    
    signal = fisher.shift(1)
    
    return pd.DataFrame({
        'Fisher': fisher,
        'Signal': signal
    })

# Example usage:
# fisher_results = calculate_ehlers_fisher(close_prices)
# print(fisher_results)
