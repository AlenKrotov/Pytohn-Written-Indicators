import numpy as np
import pandas as pd

def tema(data, period=20, column='close'):
    ema1 = data[column].ewm(span=period, adjust=False).mean()
    ema2 = ema1.ewm(span=period, adjust=False).mean()
    ema3 = ema2.ewm(span=period, adjust=False).mean()
    tema = 3 * ema1 - 3 * ema2 + ema3
    return tema

# Example usage
# df = pd.DataFrame({'close': np.random.randn(100).cumsum()})
# df['TEMA'] = tema(df, period=20)
# print(df.tail())
