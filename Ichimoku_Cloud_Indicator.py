import pandas as pd
import numpy as np

def calculate_ichimoku_cloud(high, low, close, tenkan_period=9, kijun_period=26, senkou_b_period=52, chikou_period=26):
    """
    Calculate the Ichimoku Cloud indicator.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    close (pd.Series): Closing prices for the period.
    tenkan_period (int): Period for Tenkan-sen (Conversion Line).
    kijun_period (int): Period for Kijun-sen (Base Line).
    senkou_b_period (int): Period for Senkou Span B.
    chikou_period (int): Period for Chikou Span (Lagging Span).
    
    Returns:
    pd.DataFrame: A DataFrame containing Ichimoku Cloud components.
    """
    
    # Tenkan-sen (Conversion Line): (9-period high + 9-period low) / 2
    tenkan_sen = (high.rolling(window=tenkan_period).max() + low.rolling(window=tenkan_period).min()) / 2
    
    # Kijun-sen (Base Line): (26-period high + 26-period low) / 2
    kijun_sen = (high.rolling(window=kijun_period).max() + low.rolling(window=kijun_period).min()) / 2
    
    # Senkou Span A (Leading Span A): (Conversion Line + Base Line) / 2
    senkou_span_a = ((tenkan_sen + kijun_sen) / 2).shift(kijun_period)
    
    # Senkou Span B (Leading Span B): (52-period high + 52-period low) / 2
    senkou_span_b = ((high.rolling(window=senkou_b_period).max() + low.rolling(window=senkou_b_period).min()) / 2).shift(kijun_period)
    
    # Chikou Span (Lagging Span): Close shifted back 26 periods
    chikou_span = close.shift(-chikou_period)
    
    ichimoku_df = pd.DataFrame({
        'Tenkan-sen': tenkan_sen,
        'Kijun-sen': kijun_sen,
        'Senkou Span A': senkou_span_a,
        'Senkou Span B': senkou_span_b,
        'Chikou Span': chikou_span
    })
    
    return ichimoku_df

# Example usage:
# ichimoku_results = calculate_ichimoku_cloud(high_prices, low_prices, close_prices)
# print(ichimoku_results)
