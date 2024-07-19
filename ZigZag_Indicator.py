import pandas as pd
import numpy as np

def calculate_zigzag(close, deviation=5, backstep=3):
    """
    Calculate the ZigZag indicator.

    Parameters:
    close (pd.Series): Series of closing prices.
    deviation (float): The minimum percentage change for a pivot.
    backstep (int): The number of periods to look back for calculating pivots.

    Returns:
    pd.Series: A Series containing the ZigZag values.
    """
    deviation = deviation / 100
    last_high = last_low = close.iloc[0]
    zigzag = pd.Series(index=close.index)
    trend = 1  # 1 for uptrend, -1 for downtrend

    for i in range(len(close)):
        if trend == 1:  # Looking for a new high
            if close.iloc[i] > last_high:
                last_high = close.iloc[i]
            elif close.iloc[i] < last_high * (1 - deviation):
                zigzag.iloc[i-backstep:i+1] = last_high
                trend = -1
                last_low = close.iloc[i]
        else:  # Looking for a new low
            if close.iloc[i] < last_low:
                last_low = close.iloc[i]
            elif close.iloc[i] > last_low * (1 + deviation):
                zigzag.iloc[i-backstep:i+1] = last_low
                trend = 1
                last_high = close.iloc[i]

    return zigzag

# Example usage:
# zigzag = calculate_zigzag(close_prices)
