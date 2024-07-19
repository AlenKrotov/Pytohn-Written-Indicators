import pandas as pd

def calculate_disparity_index(close, period=14):
    """
    Calculate the Disparity Index.

    Parameters:
    close (pd.Series): Series of closing prices.
    period (int): The period for the moving average calculation.

    Returns:
    pd.Series: A Series containing the Disparity Index values.
    """
    ma = close.rolling(window=period).mean()
    disparity = (close / ma - 1) * 100
    return disparity

# Example usage:
# Assuming you have a pandas Series of closing prices named 'close_prices'
# disparity_index = calculate_disparity_index(close_prices)
# print(disparity_index)
