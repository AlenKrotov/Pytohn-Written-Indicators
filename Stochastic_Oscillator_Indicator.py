import pandas as pd
import numpy as np

def calculate_stochastic_oscillator(high, low, close, k_period=14, d_period=3):
    """
    Calculate the Stochastic Oscillator indicator.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    k_period (int): The number of periods to use for the %K calculation.
    d_period (int): The number of periods to use for the %D calculation.
    
    Returns:
    pd.DataFrame: A DataFrame containing %K and %D values.
    """
    
    # Calculate %K
    lowest_low = low.rolling(window=k_period).min()
    highest_high = high.rolling(window=k_period).max()
    
    k = 100 * ((close - lowest_low) / (highest_high - lowest_low))
    
    # Calculate %D
    d = k.rolling(window=d_period).mean()
    
    # Combine the results into a DataFrame
    stoch_df = pd.DataFrame({
        '%K': k,
        '%D': d
    })
    
    return stoch_df

# Example usage:
# Assuming you have pandas Series of high, low, and closing prices named 'high_prices', 'low_prices', and 'close_prices'
# stoch_results = calculate_stochastic_oscillator(high_prices, low_prices, close_prices)
# print(stoch_results)
