import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load raw data
data = pd.read_csv('data/artists_data.csv')

# Drop rows with missing values
data = data.dropna()

# Normalize continuous features
scaler = MinMaxScaler()
