import pandas as pd
import numpy as np

def calculate_pivot_points(high, low, close):
    """
    Calculate Pivot Points and associated support/resistance levels.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.

    Returns:
    pd.DataFrame: A DataFrame containing Pivot Point, Support, and Resistance levels.
    """
    pivot_point = (high + low + close) / 3
    support1 = 2 * pivot_point - high
    support2 = pivot_point - (high - low)
    resistance1 = 2 * pivot_point - low
    resistance2 = pivot_point + (high - low)

    return pd.DataFrame({
        'Pivot Point': pivot_point,
        'Support 1': support1,
        'Support 2': support2,
        'Resistance 1': resistance1,
        'Resistance 2': resistance2
    })

# Example usage:
# pivot_points = calculate_pivot_points(high_prices, low_prices, close_prices)
