import pandas as pd
import numpy as np

def calculate_coppock_curve(close, roc1_period=14, roc2_period=11, wma_period=10):
    """
    Calculate the Coppock Curve.
    
    Parameters:
    close (pd.Series): Closing prices for the period.
    roc1_period (int): The number of periods for the first ROC calculation.
    roc2_period (int): The number of periods for the second ROC calculation.
    wma_period (int): The number of periods for the WMA calculation.
    
    Returns:
    pd.Series: A Series containing Coppock Curve values.
    """
    
    roc1 = close.pct_change(roc1_period)
    roc2 = close.pct_change(roc2_period)
    roc_sum = roc1 + roc2
    
    weights = np.arange(1, wma_period + 1)
    coppock = roc_sum.rolling(window=wma_period).apply(lambda x: np.dot(x, weights) / weights.sum())
    
    return pd.Series(coppock, name='Coppock Curve')

# Example usage:
# coppock_results = calculate_coppock_curve(close_prices)
# print(coppock_results)
