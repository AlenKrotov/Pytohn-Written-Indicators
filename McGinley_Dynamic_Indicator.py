import pandas as pd
import numpy as np

def calculate_mcginley_dynamic(close, period=14):
    """
    Calculate the McGinley Dynamic indicator.
    
    Parameters:
    close (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the calculation.
    
    Returns:
    pd.Series: A Series containing McGinley Dynamic values.
    """
    
    md = pd.Series(index=close.index)
    md.iloc[0] = close.iloc[0]
    
    for i in range(1, len(close)):
        md.iloc[i] = md.iloc[i-1] + (close.iloc[i] - md.iloc[i-1]) / (period * pow(close.iloc[i] / md.iloc[i-1], 4))
    
    return pd.Series(md, name='McGinley Dynamic')

# Example usage:
# mcginley_results = calculate_mcginley_dynamic(close_prices)
# print(mcginley_results)
