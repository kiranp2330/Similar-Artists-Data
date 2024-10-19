# similarity_calculation.py
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.metrics import jaccard_score
import numpy as np

# Load cleaned data
artist_df = pd.read_csv('cleaned_artist_data.csv')

# Define similarity function
def calculate_similarity(df):
    # Calculate Euclidean distance for continuous features
    continuous_features = ['popularity', 'followers']
    euclidean_dist = pairwise_distances(df[continuous_features], metric='euclidean')

    # Calculate Jaccard similarity for categorical features (e.g., genres)
    jaccard_sim = np.zeros((len(df), len(df)))
    for i in range(len(df)):
        for j in range(len(df)):
            jaccard_sim[i][j] = jaccard_score(df['genres'].iloc[i], df['genres'].iloc[j], average='binary')

    # Combine Euclidean and Jaccard into a final similarity score
    total_similarity = (1 - euclidean_dist) + jaccard_sim
    return total_similarity

# Run similarity calculation
similarity_scores = calculate_similarity(artist_df)

# Save similarity results
similarity_df = pd.DataFrame(similarity_scores, columns=artist_df['name'], index=artist_df['name'])
similarity_df.to_csv('artist_similarity.csv')
