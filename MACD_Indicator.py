import pandas as pd
import numpy as np

def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
    """
    Calculate the MACD (Moving Average Convergence/Divergence) values.
    
    Parameters:
    data (pd.Series): Price data, typically closing prices.
    fast_period (int): The short-term period for EMA calculation.
    slow_period (int): The long-term period for EMA calculation.
    signal_period (int): The period for signal line calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing the MACD line, signal line, and histogram.
    """
    
    # Calculate the short-term and long-term EMAs
    ema_fast = data.ewm(span=fast_period, adjust=False).mean()
    ema_slow = data.ewm(span=slow_period, adjust=False).mean()
    
    # Calculate the MACD line
    macd_line = ema_fast - ema_slow
    
    # Calculate the signal line
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    
    # Calculate the MACD histogram
    macd_histogram = macd_line - signal_line
    
    # Combine the results into a DataFrame
    macd_df = pd.DataFrame({
        'MACD': macd_line,
        'Signal': signal_line,
        'Histogram': macd_histogram
    })
    
    return macd_df

# Example usage:
# Assuming you have a pandas Series of closing prices named 'close_prices'
# macd_results = calculate_macd(close_prices)
# print(macd_results)
