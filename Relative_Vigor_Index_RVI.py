import pandas as pd
import numpy as np

def calculate_rvi(open_prices, high_prices, low_prices, close_prices, period=10):
    """
    Calculate the Relative Vigor Index (RVI).
    
    Parameters:
    open_prices (pd.Series): Opening prices for the period.
    high_prices (pd.Series): High prices for the period.
    low_prices (pd.Series): Low prices for the period.
    close_prices (pd.Series): Closing prices for the period.
    period (int): The number of periods to use for the RVI calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing RVI and Signal line values.
    """
    
    def sym_weighted_mov_avg(values, period):
        weights = np.arange(1, period + 1)
        return values.rolling(window=period).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)

    numerator = close_prices - open_prices
    denominator = high_prices - low_prices
    
    rvi = sym_weighted_mov_avg(numerator, period) / sym_weighted_mov_avg(denominator, period)
    
    signal = sym_weighted_mov_avg(rvi, 4)
    
    return pd.DataFrame({
        'RVI': rvi,
        'Signal': signal
    })

# Example usage:
# rvi_results = calculate_rvi(open_prices, high_prices, low_prices, close_prices)
# print(rvi_results)
