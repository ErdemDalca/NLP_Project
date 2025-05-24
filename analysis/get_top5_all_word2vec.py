import os
import pandas as pd
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# === Ayarlar ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_path = os.path.join(BASE_DIR, "data")
output_path = os.path.join(BASE_DIR, "analysis", "top5_outputs")
model_dir = os.path.join(BASE_DIR, "models")

# === Giriş cümleleri (lemmatized ve stemmed)
query_lemma = "powerups general every piece control even applicable opponent piece"
query_stem = "powerup gener everi piec control even applic oppon piec"

# === Veri yolları
csv_files = {
    "lemma": os.path.join(data_path, "lemmatized_sentences.csv"),
    "stem": os.path.join(data_path, "stemmed_sentences.csv")
}
column_names = {
    "lemma": "Lemmatized",
    "stem": "Stemmed"
}

# === Cümleyi vektöre dönüştür

def sentence_vector(sentence, model):
    words = sentence.split()
    vectors = [model.wv[word] for word in words if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else None

# === Tüm .model dosyaları
model_files = [f for f in os.listdir(model_dir) if f.endswith(".model")]
print(f"\n🔍 Toplam {len(model_files)} Word2Vec modeli bulundu.\n")

for model_file in model_files:
    print(f"📦 Model işleniyor: {model_file}")

    try:
        parts = model_file.replace(".model", "").split("_")
        data_type = parts[1]          # lemma / stem
        arch = parts[2]               # cbow / skipgram
        window = parts[3].replace("w", "")
        dim = parts[4].replace("d", "")
    except IndexError:
        print(f"⚠️ Geçersiz model adı formatı, atlandı: {model_file}")
        continue

    # === Giriş cümlesini belirle
    query = query_lemma if data_type == "lemma" else query_stem

    # === Veri yükle
    data_csv = csv_files.get(data_type)
    column = column_names.get(data_type)
    if data_csv is None or column is None:
        print(f"⚠️ Veri dosyası eksik: {data_type}")
        continue

    df_sentences = pd.read_csv(data_csv)
    match_index = df_sentences[df_sentences[column] == query].index
    if len(match_index) == 0:
        print(f"❌ Giriş cümlesi veri setinde bulunamadı. → {data_type}")
        continue

    query_idx = match_index[0]
    query_base_sentence = df_sentences.loc[query_idx, "Base Sentence"]

    # === Modeli yükle
    model_path = os.path.join(model_dir, model_file)
    model = Word2Vec.load(model_path)
    query_vec = sentence_vector(query, model)
    if query_vec is None:
        print("❌ Giriş cümlesindeki kelimeler modelde bulunamadı.")
        continue

    # === Tüm cümle vektörleri
    sentence_vectors = []
    valid_indexes = []
    for idx, sent in enumerate(df_sentences[column]):
        vec = sentence_vector(sent, model)
        if vec is not None:
            sentence_vectors.append(vec)
            valid_indexes.append(idx)

    if not sentence_vectors:
        print("⚠️ Geçerli cümle vektörü bulunamadı.")
        continue

    matrix = np.vstack(sentence_vectors)
    query_vector = query_vec.reshape(1, -1)
    scores = cosine_similarity(query_vector, matrix)[0]

    top5_relative = scores.argsort()[::-1][1:6]
    top5_idx = [valid_indexes[i] for i in top5_relative]

    top5_df = df_sentences.iloc[top5_idx][["Game", "Base Sentence"]].copy()
    top5_df.insert(0, "Match Index", top5_idx)
    top5_df["Similarity Score"] = scores[top5_relative]
    top5_df.insert(1, "Query Index", query_idx)

    meta_row = pd.DataFrame([{
        "Match Index": query_idx,
        "Query Index": query_idx,
        "Game": "GIRIS CUMLESI",
        "Base Sentence": query_base_sentence,
        "Similarity Score": 1.0
    }])

    final_df = pd.concat([meta_row, top5_df], ignore_index=True)
    os.makedirs(output_path, exist_ok=True)

    file_short = f"{data_type}_{arch}_w{window}_d{dim}"
    out_file = os.path.join(output_path, f"top5_w2v_{file_short}.csv")
    final_df.to_csv(out_file, index=False)

    print(f"✅ Kaydedildi → {out_file}\n")
