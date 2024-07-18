def calculate_williams_fractal(high, low):
    """
    Calculate the Williams Fractal indicator.
    
    Parameters:
    high (pd.Series): High prices for the period.
    low (pd.Series): Low prices for the period.
    
    Returns:
    pd.DataFrame: A DataFrame containing Bullish and Bearish Fractal signals.
    """
    
    bullish_fractal = pd.Series(np.zeros(len(high)), index=high.index)
    bearish_fractal = pd.Series(np.zeros(len(low)), index=low.index)
    
    for i in range(2, len(high) - 2):
        if (low[i] < low[i-1] and low[i] < low[i-2] and 
            low[i] < low[i+1] and low[i] < low[i+2]):
            bullish_fractal.iloc[i] = 1
        
        if (high[i] > high[i-1] and high[i] > high[i-2] and 
            high[i] > high[i+1] and high[i] > high[i+2]):
            bearish_fractal.iloc[i] = 1
    
    return pd.DataFrame({
        'Bullish Fractal': bullish_fractal,
        'Bearish Fractal': bearish_fractal
    })

# Example usage:
# fractal_results = calculate_williams_fractal(high_prices, low_prices)
# print(fractal_results)
