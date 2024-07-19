import pandas as pd
import numpy as np

def calculate_roc(close, period=14):
    """
    Calculate the Rate of Change (ROC).

    Parameters:
    close (pd.Series): Series of closing prices.
    period (int): The period over which to calculate the ROC.

    Returns:
    pd.Series: A Series containing the ROC values.
    """
    # Calculate ROC
    roc = ((close - close.shift(period)) / close.shift(period)) * 100

    return roc
