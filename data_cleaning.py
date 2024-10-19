# data_cleaning.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data
artist_df = pd.read_csv('artist_data.csv')

# Handling missing values
artist_df.fillna(method='ffill', inplace=True)

# Scaling continuous features (popularity, followers)
scaler = StandardScaler()
artist_df[['popularity', 'followers']] = scaler.fit_transform(artist_df[['popularity', 'followers']])

# Handling outliers (capping at 95th percentile)
for col in ['popularity', 'followers']:
    upper_limit = artist_df[col].quantile(0.95)
    artist_df[col] = artist_df[col].apply(lambda x: min(x, upper_limit))

# Save the cleaned data
artist_df.to_csv('cleaned_artist_data.csv', index=False)
