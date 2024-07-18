import pandas as pd
import numpy as np

def calculate_keltner_channels(high, low, close, ema_period=20, atr_period=10, multiplier=2):
    """
    Calculate Keltner Channels.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    ema_period (int): The number of periods to use for the EMA calculation.
    atr_period (int): The number of periods to use for the ATR calculation.
    multiplier (float): Multiplier for the ATR to set channel width.
    
    Returns:
    pd.DataFrame: A DataFrame containing Upper, Middle, and Lower Keltner Channel values.
    """
    
    def calculate_atr(high, low, close, period):
        tr = pd.DataFrame(index=high.index)
        tr['h-l'] = high - low
        tr['h-pc'] = abs(high - close.shift(1))
        tr['l-pc'] = abs(low - close.shift(1))
        tr['tr'] = tr[['h-l', 'h-pc', 'l-pc']].max(axis=1)
        return tr['tr'].rolling(period).mean()

    middle_line = close.ewm(span=ema_period, adjust=False).mean()
    atr = calculate_atr(high, low, close, atr_period)
    
    upper_line = middle_line + multiplier * atr
    lower_line = middle_line - multiplier * atr
    
    return pd.DataFrame({
        'Upper': upper_line,
        'Middle': middle_line,
        'Lower': lower_line
    })

# Example usage:
# keltner_results = calculate_keltner_channels(high_prices, low_prices, close_prices)
# print(keltner_results)
