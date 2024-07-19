import pandas as pd
import numpy as np

def calculate_adx(high, low, close, period=14):
    """
    Calculate the Average Directional Index (ADX).

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    period (int): The period over which to calculate the ADX.

    Returns:
    pd.DataFrame: A DataFrame containing ADX, +DI, and -DI values.
    """
    # Calculate True Range
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate Directional Movement
    up_move = high - high.shift(1)
    down_move = low.shift(1) - low
    pos_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
    neg_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)

    # Calculate smoothed TR and DM
    smoothed_tr = tr.rolling(window=period).sum()
    smoothed_pos_dm = pd.Series(pos_dm).rolling(window=period).sum()
    smoothed_neg_dm = pd.Series(neg_dm).rolling(window=period).sum()

    # Calculate Directional Indicators
    pdi = 100 * smoothed_pos_dm / smoothed_tr
    ndi = 100 * smoothed_neg_dm / smoothed_tr

    # Calculate Directional Index
    dx = 100 * abs(pdi - ndi) / (pdi + ndi)

    # Calculate ADX
    adx = dx.rolling(window=period).mean()

    return pd.DataFrame({'ADX': adx, '+DI': pdi, '-DI': ndi})

# Example usage:
# adx_values = calculate_adx(high_prices, low_prices, close_prices)
