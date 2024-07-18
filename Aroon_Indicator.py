import pandas as pd
import numpy as np

def calculate_aroon(high, low, period=14):
    """
    Calculate the Aroon Indicator.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    period (int): The number of periods to use for the Aroon calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing Aroon Up and Aroon Down values.
    """
    
    aroon_up = 100 * high.rolling(period + 1).apply(lambda x: x.argmax()) / period
    aroon_down = 100 * low.rolling(period + 1).apply(lambda x: x.argmin()) / period
    
    return pd.DataFrame({
        'Aroon Up': aroon_up,
        'Aroon Down': aroon_down
    })

# Example usage:
# aroon_results = calculate_aroon(high_prices, low_prices)
# print(aroon_results)
