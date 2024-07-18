import numpy as np
import pandas as pd

def cmo(data, period=14, column='close'):
    delta = data[column].diff()
    
    up = delta.where(delta > 0, 0).rolling(window=period).sum()
    down = -delta.where(delta < 0, 0).rolling(window=period).sum()
    
    cmo = 100 * (up - down) / (up + down)
    return cmo

# Example usage:
# df = pd.DataFrame({'close': np.random.randn(100).cumsum()})
# df['CMO'] = cmo(df, period=14)
# print(df.tail())
