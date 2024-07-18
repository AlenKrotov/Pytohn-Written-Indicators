import pandas as pd
import numpy as np

def calculate_parabolic_sar(high, low, step=0.02, max_step=0.2):
    """
    Calculate the Parabolic SAR (Stop and Reverse).
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    step (float): The step value used to calculate the SAR.
    max_step (float): The maximum step value.
    
    Returns:
    pd.Series: A Series containing Parabolic SAR values.
    """
    
    sar = pd.Series(index=high.index)
    ep = pd.Series(index=high.index)
    af = pd.Series(index=high.index)
    
    bull = True
    sar.iloc[0] = low.iloc[0]
    ep.iloc[0] = high.iloc[0]
    af.iloc[0] = step
    
    for i in range(1, len(high)):
        if bull:
            sar.iloc[i] = sar.iloc[i-1] + af.iloc[i-1] * (ep.iloc[i-1] - sar.iloc[i-1])
            if low.iloc[i] < sar.iloc[i]:
                bull = False
                sar.iloc[i] = ep.iloc[i-1]
                ep.iloc[i] = low.iloc[i]
                af.iloc[i] = step
            else:
                if high.iloc[i] > ep.iloc[i-1]:
                    ep.iloc[i] = high.iloc[i]
                    af.iloc[i] = min(af.iloc[i-1] + step, max_step)
                else:
                    ep.iloc[i] = ep.iloc[i-1]
                    af.iloc[i] = af.iloc[i-1]
        else:
            sar.iloc[i] = sar.iloc[i-1] - af.iloc[i-1] * (sar.iloc[i-1] - ep.iloc[i-1])
            if high.iloc[i] > sar.iloc[i]:
                bull = True
                sar.iloc[i] = ep.iloc[i-1]
                ep.iloc[i] = high.iloc[i]
                af.iloc[i] = step
            else:
                if low.iloc[i] < ep.iloc[i-1]:
                    ep.iloc[i] = low.iloc[i]
                    af.iloc[i] = min(af.iloc[i-1] + step, max_step)
                else:
                    ep.iloc[i] = ep.iloc[i-1]
                    af.iloc[i] = af.iloc[i-1]
    
    return pd.Series(sar, name='SAR')

# Example usage:
# sar_results = calculate_parabolic_sar(high_prices, low_prices)
# print(sar_results)
