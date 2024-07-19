import pandas as pd
import numpy as np

def calculate_rsi(data, period=14):
    """
    Calculate the Relative Strength Index (RSI).

    Parameters:
    data (pd.Series): Price data, typically closing prices.
    period (int): The period over which to calculate the RSI.

    Returns:
    pd.Series: A Series containing the RSI values.
    """
    # Calculate price changes
    delta = data.diff()

    # Separate gains and losses
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    # Calculate RS and RSI
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi
