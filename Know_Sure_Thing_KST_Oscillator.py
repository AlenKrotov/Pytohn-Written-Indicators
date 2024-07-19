import pandas as pd
import numpy as np

def calculate_kst(close, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, nsig=9):
    """
    Calculate the Know Sure Thing (KST) oscillator.

    Parameters:
    close (pd.Series): Series of closing prices.
    r1, r2, r3, r4 (int): Periods for the rate-of-change calculations.
    n1, n2, n3, n4 (int): Smoothing periods for the rate-of-change calculations.
    nsig (int): Signal line period.

    Returns:
    pd.DataFrame: A DataFrame containing KST and its signal line.
    """
    rocma1 = close.diff(r1).rolling(n1).mean()
    rocma2 = close.diff(r2).rolling(n2).mean()
    rocma3 = close.diff(r3).rolling(n3).mean()
    rocma4 = close.diff(r4).rolling(n4).mean()
    
    kst = 100 * (rocma1 + 2 * rocma2 + 3 * rocma3 + 4 * rocma4)
    sig = kst.rolling(nsig).mean()
    
    return pd.DataFrame({'KST': kst, 'Signal': sig})

# Example usage:
# kst = calculate_kst(close_prices)
