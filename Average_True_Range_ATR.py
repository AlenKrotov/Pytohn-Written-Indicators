import pandas as pd
import numpy as np

def calculate_atr(high, low, close, period=14):
    """
    Calculate the Average True Range (ATR).

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    period (int): The period over which to calculate the ATR.

    Returns:
    pd.Series: A Series containing the ATR values.
    """
    # Calculate True Range
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate ATR
    atr = tr.rolling(window=period).mean()

    return atr
