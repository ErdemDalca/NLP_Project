import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import sparse
import joblib

# === Ayarlar ===
base_dir = os.path.dirname(__file__)
output_dir = os.path.join(base_dir, "..", "vector_outputs")

os.makedirs(output_dir, exist_ok=True)

input_files = {
    "lemma": os.path.join(base_dir, "..", "data", "lemmatized_sentences.csv"),
    "stem": os.path.join(base_dir, "..", "data", "stemmed_sentences.csv")
}
column_names = {
    "lemma": "Lemmatized",
    "stem": "Stemmed"
}

# === Her veri tipi için tam TF-IDF oluştur
for dtype in ["lemma", "stem"]:
    print(f"\n🔄 Başlıyor: {dtype.upper()}")

    # Dosya yolları
    csv_path = input_files[dtype]
    column = column_names[dtype]
    output_npz = os.path.join(output_dir, f"tfidf_full_{dtype}.npz")
    output_vectorizer = os.path.join(output_dir, f"tfidf_vectorizer_{dtype}.pkl")

    # Veriyi oku
    df = pd.read_csv(csv_path)
    sentences = df[column].dropna().tolist()
    sentences = [" ".join(s.strip().split()) for s in sentences]

    # TF-IDF hesapla (tüm vocabulary)
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(sentences)  # sparse matrix

    # Sparse matrisi kaydet
    sparse.save_npz(output_npz, matrix)

    # Vectorizer objesini sakla (kelimeler + IDF değerleri için)
    joblib.dump(vectorizer, output_vectorizer)

    print(f"✅ TF-IDF matrisi kaydedildi: {output_npz}")
    print(f"✅ TF-IDF vectorizer kaydedildi: {output_vectorizer}")
    print(f"🔢 Vektör boyutu: {matrix.shape} (satır=cümle, sütun=kelime)")
