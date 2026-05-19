import pandas as pd

def load_csv(path):
    """Loads a CSV file from the specified path and returns a pandas DataFrame."""
    return pd.read_csv(path)
