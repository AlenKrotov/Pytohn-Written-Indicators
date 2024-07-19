import pandas as pd
import numpy as np

def calculate_obv(close, volume):
    """
    Calculate the On-Balance Volume (OBV).

    Parameters:
    close (pd.Series): Series of closing prices.
    volume (pd.Series): Series of volume data.

    Returns:
    pd.Series: A Series containing the OBV values.
    """
    # Calculate OBV
    obv = np.where(close > close.shift(1), volume, 
                   np.where(close < close.shift(1), -volume, 0)).cumsum()
    
    return pd.Series(obv, name='OBV')
