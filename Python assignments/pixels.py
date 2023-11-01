

# Given vectors
D = np.array([0.6, 0.8, 0, 0.2])
Q = np.array([0.4, 0.6, 0.1, 0])

# Calculate dot product of D and Q
dot_product = np.dot(D, Q)

# Calculate magnitudes (Euclidean norms)
magnitude_D = np.linalg.norm(D)
magnitude_Q = np.linalg.norm(Q)

# Calculate cosine similarity
cosine_similarity = dot_product / (magnitude_D * magnitude_Q)

# Display the result
print(f"The cosine similarity between the document and the query is approximately {cosine_similarity:.2f}")





