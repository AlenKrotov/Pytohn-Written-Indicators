import pandas as pd
import numpy as np

def calculate_fractal_dimension_index(high, low, period=30):
    """
    Calculate the Fractal Dimension Index (FDI).

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    period (int): The period over which to calculate the FDI.

    Returns:
    pd.Series: A Series containing the FDI values.
    """
    def fdi(h, l):
        n = len(h)
        hilo = np.log(h.max()) - np.log(l.min())
        if hilo == 0:
            return 1
        
        closes = np.array(range(n))
        closeslog = np.log(closes + 1)
        
        m = (closeslog[-1] - closeslog[0]) / (closes[-1] - closes[0])
        b = closeslog[0]
        
        hest = np.exp(m * closes + b)
        lest = np.exp(m * closes + b - hilo)
        
        highs = np.log(h) - np.log(hest)
        lows = np.log(lest) - np.log(l)
        
        highs = highs[np.isfinite(highs)]
        lows = lows[np.isfinite(lows)]
        
        return 1 + (np.log(np.sum(np.sqrt(highs**2 + lows**2)) / np.sqrt(2 * n)) / np.log(2))
    
    return high.rolling(period).agg(fdi, args=(low,))

# Example usage:
# fdi = calculate_fractal_dimension_index(high_prices, low_prices)
