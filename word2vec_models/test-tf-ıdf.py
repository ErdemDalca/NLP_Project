import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df = pd.read_csv(r"word2vec_models\tfidf_filtered_lemmatized.csv", index_col=0)

target_word = "gam"

if target_word not in df.columns:
    raise ValueError(f"'{target_word}' kelimesi bulunamadı.")

# Sadece target vektörü ve kolonları al
target_vector = df[target_word].values.reshape(1, -1)
matrix = df.T.values  # shape: (kelime sayısı, belge sayısı)

# Normalize etmeden cosine similarity uygula
similarities = cosine_similarity(target_vector, matrix)[0]

# En benzer 10 kelime
top_indices = similarities.argsort()[::-1][1:11]
top_words = df.columns[top_indices]
top_scores = similarities[top_indices]

print(f"🔍 '{target_word}' kelimesine en benzer 10 kelime:")
for word, score in zip(top_words, top_scores):
    print(f"{word}: {score:.4f}")
