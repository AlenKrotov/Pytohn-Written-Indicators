import pandas as pd

def calculate_wave_trend_oscillator(high, low, close, channel_length=10, average_length=21):
    """
    This is a trend-following momentum indicator that combines the techniques of MACD and RSI. It's designed to spot overbought and oversold conditions as well as trend direction.

    Calculate the WaveTrend Oscillator.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    close (pd.Series): Series of closing prices.
    channel_length (int): The period for the initial calculations.
    average_length (int): The period for the final smoothing.

    Returns:
    pd.DataFrame: A DataFrame containing the WaveTrend Oscillator values and its signal line.
    """
    ap = (high + low + close) / 3
    esa = ap.ewm(span=channel_length).mean()
    d = (ap - esa).abs().ewm(span=channel_length).mean()
    ci = (ap - esa) / (0.015 * d)
    wt1 = ci.ewm(span=average_length).mean()
    wt2 = wt1.rolling(window=4).mean()
    
    return pd.DataFrame({'WT1': wt1, 'WT2': wt2})

# Example usage:
# Assuming you have pandas Series of prices named 'high_prices', 'low_prices', and 'close_prices'
# wavetrend = calculate_wave_trend_oscillator(high_prices, low_prices, close_prices)
# print(wavetrend)
