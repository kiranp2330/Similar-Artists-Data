# data_collection.py
import requests
import pandas as pd

# Function to get artist data from Spotify API
def get_spotify_data(artist_name, token):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Extract relevant data
    artist_data = {
        'name': artist_name,
        'genres': data['artists']['items'][0]['genres'],
        'popularity': data['artists']['items'][0]['popularity'],
        'followers': data['artists']['items'][0]['followers']['total'],
        'years_active': data['artists']['items'][0]['followers']['total'],  # This needs refinement
    }
    
    return artist_data

# Example usage:
token = "your_spotify_api_token"
artists = ["Drake", "J. Cole", "Travis Scott"]
artist_data = [get_spotify_data(artist, token) for artist in artists]

# Convert to DataFrame
artist_df = pd.DataFrame(artist_data)
artist_df.to_csv("artist_data.csv", index=False)
