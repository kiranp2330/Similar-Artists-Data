# visualization.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load similarity data
similarity_df = pd.read_csv('artist_similarity.csv', index_col=0)

# Plot a heatmap for similarity scores
plt.figure(figsize=(10, 8))
sns.heatmap(similarity_df, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Artist Similarity Heatmap')
plt.show()

# Save the plot
plt.savefig('artist_similarity_heatmap.png')
