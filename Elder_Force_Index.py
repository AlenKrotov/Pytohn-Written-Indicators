import numpy as np
import pandas as pd

def elder_force_index(data, period=13):
    fi = (data['close'] - data['close'].shift(1)) * data['volume']
    efi = fi.ewm(span=period, adjust=False).mean()
    return efi

# Example usage:
# df = pd.DataFrame({
#     'close': np.random.randn(100).cumsum(),
#     'volume': np.random.randint(1000, 10000, 100)
# })
# df['EFI'] = elder_force_index(df, period=13)
# print(df.tail())
