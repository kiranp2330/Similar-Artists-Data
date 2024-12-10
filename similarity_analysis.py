import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import MultiLabelBinarizer

def calculate_similarity(query_artist, data):
    # Separate categorical and continuous features
    categorical_features = ['Genres', 'LyricalThemes']
    continuous_features = ['Popularity', 'Followers', 'YearsActive']
    
    # Process categorical features with Jaccard similarity
    mlb = MultiLabelBinarizer()
    categorical_data = data[categorical_features].apply(lambda x: x.str.split(', '))
    categorical_data = pd.DataFrame(mlb.fit_transform(categorical_data.values.ravel()),
                                    columns=mlb.classes_, index=data.index)
    
    # Combine processed features
    processed_data = pd.concat([data[continuous_features], categorical_data], axis=1)
    
    # Compute Euclidean distances for continuous features
    query_vector = processed_data.loc[query_artist].values.reshape(1, -1)
    distances = euclidean_distances(processed_data, query_vector).flatten()
    
    # Combine distance scores
    data['SimilarityScore'] = distances
    return data.sort_values('SimilarityScore').iloc[1:11]  # Exclude the query artist

# Load cleaned data
data = pd.read_csv('data/cleaned_artists_data.csv')

# Query for Drake
drake_results = calculate_similarity(data[data['ArtistName'] == 'Drake'].index[0], data)
drake_results.to_csv('data/similar_to_drake.csv', index=False)

# Query for Taylor Swift
taylor_results = calculate_similarity(data[data['ArtistName'] == 'Taylor Swift'].index[0], data)
taylor_results.to_csv('data/similar_to_taylor_swift.csv', index=False)

# Query for Kanye West
kanye_results = calculate_similarity(data[data['ArtistName'] == 'Kanye West'].index[0], data)
kanye_results.to_csv('data/similar_to_kanye_west.csv', index=False)

print("Similarity analysis complete. Results saved to CSV files.")
