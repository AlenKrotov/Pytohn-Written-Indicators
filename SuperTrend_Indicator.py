import pandas as pd
import numpy as np

def calculate_supertrend(high, low, close, period=14, multiplier=3):
    """
    Calculate the SuperTrend indicator.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    period (int): The period for ATR calculation.
    multiplier (float): The multiplier for the ATR.

    Returns:
    pd.DataFrame: A DataFrame containing SuperTrend values and direction.
    """
    atr = calculate_atr(high, low, close, period)
    
    hl2 = (high + low) / 2
    upper_band = hl2 + (multiplier * atr)
    lower_band = hl2 - (multiplier * atr)
    
    supertrend = pd.Series(index=close.index, dtype=float)
    direction = pd.Series(index=close.index, dtype=int)
    
    for i in range(period, len(close)):
        if close.iloc[i] > upper_band.iloc[i-1]:
            supertrend.iloc[i] = lower_band.iloc[i]
            direction.iloc[i] = 1
        elif close.iloc[i] < lower_band.iloc[i-1]:
            supertrend.iloc[i] = upper_band.iloc[i]
            direction.iloc[i] = -1
        else:
            supertrend.iloc[i] = supertrend.iloc[i-1]
            direction.iloc[i] = direction.iloc[i-1]
            
            if (direction.iloc[i] == 1 and lower_band.iloc[i] < supertrend.iloc[i]):
                supertrend.iloc[i] = lower_band.iloc[i]
            elif (direction.iloc[i] == -1 and upper_band.iloc[i] > supertrend.iloc[i]):
                supertrend.iloc[i] = upper_band.iloc[i]
    
    return pd.DataFrame({'SuperTrend': supertrend, 'Direction': direction})

# Example usage:
# supertrend = calculate_supertrend(high_prices, low_prices, close_prices)
