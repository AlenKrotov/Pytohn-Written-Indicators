import numpy as np
import pandas as pd

def kama(data, period=10, fast=2, slow=30, column='close'):
    change = abs(data[column].diff())
    volatility = change.rolling(period).sum()
    
    efficiency_ratio = abs(data[column].diff(period)) / volatility
    smoothing_constant = (efficiency_ratio * (2.0/(fast+1) - 2.0/(slow+1)) + 2.0/(slow+1))**2
    
    kama = np.zeros_like(data[column])
    kama[period-1] = data[column].iloc[period-1]
    for i in range(period, len(data)):
        kama[i] = kama[i-1] + smoothing_constant[i] * (data[column].iloc[i] - kama[i-1])
    
    return pd.Series(kama, name='KAMA')

# Example usage:
# df = pd.DataFrame({'close': np.random.randn(100).cumsum()})
# df['KAMA'] = kama(df, period=10, fast=2, slow=30)
# print(df.tail())
