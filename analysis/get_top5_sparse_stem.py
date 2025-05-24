import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import joblib

# === Ayarlar ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
tfidf_matrix_path = os.path.join(BASE_DIR, "vector_outputs", "tfidf_full_stem.npz")
tfidf_vectorizer_path = os.path.join(BASE_DIR, "vector_outputs", "tfidf_vectorizer_stem.pkl")
sentences_path = os.path.join(BASE_DIR, "data", "stemmed_sentences.csv")
output_path = os.path.join(BASE_DIR, "analysis", "top5_outputs", "top5_sparse_stem.csv")

# === Giriş cümlesi (stemmed haliyle) — dikkat: tam eşleşmeli olmalı
query = "powerup gener everi piec control even applic oppon piec"

# === Veriyi yükle
df_sentences = pd.read_csv(sentences_path)
match_index = df_sentences[df_sentences["Stemmed"] == query].index

if len(match_index) == 0:
    print("❌ Giriş cümlesi veri setinde bulunamadı.")
    exit()

query_idx = match_index[0]
query_base_sentence = df_sentences.loc[query_idx, "Base Sentence"]

# === TF-IDF matrisi ve vectorizer'ı yükle
matrix = sparse.load_npz(tfidf_matrix_path)
vectorizer = joblib.load(tfidf_vectorizer_path)

# === Vektörü çıkar
query_vector = matrix[query_idx]

if query_vector.nnz == 0:
    print("⚠️ Uyarı: Giriş cümlesi için TF-IDF vektörü tamamen sıfır.")
    exit()

# === Cosine similarity hesapla
scores = cosine_similarity(query_vector, matrix)[0]

# === En benzer 5 (kendisi hariç)
top5_idx = scores.argsort()[::-1][1:6]

# === Çıktı oluştur
top5_df = df_sentences.iloc[top5_idx][["Game", "Base Sentence"]].copy()
top5_df["Similarity Score"] = scores[top5_idx]
top5_df.insert(0, "Match Index", top5_idx)
top5_df.insert(1, "Query Index", query_idx)

# === Giriş cümlesi bilgisi üst satıra eklenecek
meta_row = pd.DataFrame([{
    "Match Index": query_idx,
    "Query Index": query_idx,
    "Game": "GIRIS CUMLESI",
    "Base Sentence": query_base_sentence,
    "Similarity Score": 1.0
}])

# === Birleştir ve kaydet
final_df = pd.concat([meta_row, top5_df], ignore_index=True)
os.makedirs(os.path.dirname(output_path), exist_ok=True)
final_df.to_csv(output_path, index=False)

print(f"✅ En benzer 5 cümle ve giriş cümlesi başarıyla kaydedildi → {output_path}")
