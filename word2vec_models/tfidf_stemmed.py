import os
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer

# === Yol ayarları
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "..", "processed_sentences.csv")
model_path = os.path.join(base_dir, "word2vec_stemmed_skipgram_w10_d300.model")
output_path = os.path.join(base_dir, "tfidf_filtered_stemmed.csv")

# === Veri yükle
df = pd.read_csv(csv_path)
sentences = df["Stemmed"].dropna().tolist()

# === Modeli yükle
model = Word2Vec.load(model_path)

# === 'game' kelimesine benzer 100 kelimeyi al
similar_words = [word for word, _ in model.wv.most_similar("game", topn=1000)]

# === TF-IDF hesapla
vectorizer = TfidfVectorizer(vocabulary=similar_words)
matrix = vectorizer.fit_transform(sentences)
df_tfidf = pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names_out())

# === CSV olarak kaydet
df_tfidf.to_csv(output_path, index=False)
print(f"✅ Stemmed için TF-IDF dosyası kaydedildi: {output_path}")
