import numpy as np
import pandas as pd

def bollinger_bands_pct_b(data, period=20, std=2, column='close'):
    rolling_mean = data[column].rolling(window=period).mean()
    rolling_std = data[column].rolling(window=period).std()
    
    upper_band = rolling_mean + (rolling_std * std)
    lower_band = rolling_mean - (rolling_std * std)
    
    bb_b = (data[column] - lower_band) / (upper_band - lower_band)
    return bb_b

# Example usage:
# df = pd.DataFrame({'close': np.random.randn(100).cumsum()})
# df['BB_%B'] = bollinger_bands_pct_b(df, period=20, std=2)
# print(df.tail())
