import pandas as pd
from shared import df
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt

#FIXME: REFACTOR CODE SO THE IMPORTS DO NOT NEED TO BE REPEATED in EVERY FILE IN THIS FOLDER.

#change the catagorical def into more numeric output
encoder = OneHotEncoder(sparse_output=False)
categorical_columns = ['Direction', 'Shot Type', 'Stroke','Outcome','Context']
# Check all specified categorical columns in filtered_df
for col in categorical_columns:
    if col not in df.columns:
      print(f"Warning: Column '{col}' not found in the DataFrame. Skipping encoding.")
      categorical_columns.remove(col)

#fit and transform the catagorical columns to encode
if categorical_columns:
    categorical_data = encoder.fit_transform(df[categorical_columns])
    categorical_df = pd.DataFrame(categorical_data, columns=encoder.get_feature_names_out(categorical_columns))

    filtered_df= pd.concat([df.reset_index(drop=True), categorical_df],axis=1)

#drop all irrelevant columns
columns_to_drop = categorical_columns + ['Player Name', 'Video Time', 'Rally #', 'Shot # of Rally', 'Point #']
filtered_df = filtered_df.drop(columns=[col for col in columns_to_drop if col in filtered_df.columns])

# Step 4: Scale the features to standardize them
scaler = StandardScaler()
scaled_data = scaler.fit_transform(filtered_df)

# Step 5: Determine the optimal number of clusters using the Elbow Method
inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plot the inertia to visualize the Elbow point
plt.figure(figsize=(8, 6))
plt.plot(k_range, inertia, 'bo-')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia (Sum of Squared Distances)")
plt.title("Elbow Method for Optimal k")
plt.show()

# Step 6: Run K-means with the chosen number of clusters (e.g., k=3 based on the Elbow Method)
optimal_k = 4  # Adjust this based on the elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(scaled_data)

# Add the cluster labels to the original DataFrame
filtered_df['Cluster'] = kmeans.labels_

# Display the resulting DataFrame with clusters
print(filtered_df.head())


