import pandas as pd
import numpy as np

def calculate_eom(high, low, volume, period=14):
    """
    Calculate the Ease of Movement (EOM) indicator.

    Parameters:
    high (pd.Series): Series of high prices.
    low (pd.Series): Series of low prices.
    volume (pd.Series): Series of volume data.
    period (int): The period over which to calculate the EOM.

    Returns:
    pd.Series: A Series containing the EOM values.
    """
    # Calculate distance moved
    distance = ((high + low) / 2) - ((high.shift(1) + low.shift(1)) / 2)

    # Calculate box ratio
    box_ratio = (volume / 100000000) / (high - low)

    # Calculate raw EOM
    eom = distance / box_ratio

    # Calculate the EOM indicator
    eom_indicator = eom.rolling(window=period).mean()

    return eom_indicator
