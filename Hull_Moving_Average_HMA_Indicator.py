import numpy as np
import pandas as pd

def hma(data, period=20, column='close'):
    half_period = int(period/2)
    sqrt_period = int(np.sqrt(period))
    
    wma1 = data[column].rolling(window=half_period).apply(lambda x: np.dot(x, np.arange(1, half_period+1)) / np.arange(1, half_period+1).sum())
    wma2 = data[column].rolling(window=period).apply(lambda x: np.dot(x, np.arange(1, period+1)) / np.arange(1, period+1).sum())
    
    diff = 2 * wma1 - wma2
    hma = diff.rolling(window=sqrt_period).apply(lambda x: np.dot(x, np.arange(1, sqrt_period+1)) / np.arange(1, sqrt_period+1).sum())
    
    return hma

# Example usage:
# df = pd.DataFrame({'close': np.random.randn(100).cumsum()})
# df['HMA'] = hma(df, period=20)
# print(df.tail())
