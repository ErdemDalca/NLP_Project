import os
from gensim.models import Word2Vec
import pandas as pd

# === Parametreler ===
column = "Stemmed"
window = 10
vector_size = 1000
sg = 0
current_dir = os.path.dirname(__file__)
input_path = os.path.abspath(os.path.join(current_dir, "..", "processed_sentences.csv"))

# === Veriyi oku ===
df = pd.read_csv(input_path)
sentences = df[column].dropna().apply(lambda x: x.strip().split()).tolist()

# === Modeli eğit ===
model = Word2Vec(
    sentences=sentences,
    vector_size=vector_size,
    window=window,
    min_count=2,
    workers=4,
    sg=sg
)

# === Kaydet ===
model_name = f"word2vec_stemmed_cbow_w{window}_d{vector_size}.model"
model_path = os.path.join(current_dir, model_name)
model.save(model_path)

# === TF-IDF benzeri CSV çıktısı ===
vector_out_path = os.path.join(current_dir, f"vectors_stemmed_cbow_w{window}_d{vector_size}.csv")
vectors = []
words = []

for word in model.wv.index_to_key:
    words.append(word)
    vectors.append(model.wv[word])

import pandas as pd
pd.DataFrame(vectors, index=words).to_csv(vector_out_path)

print(f"✅ Model ve vektör CSV kaydedildi: {model_name}, {vector_out_path}")
