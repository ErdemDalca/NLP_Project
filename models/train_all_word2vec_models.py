import os
import pandas as pd
from gensim.models import Word2Vec

# === Ayarlar ===
current_dir = os.path.dirname(__file__)
data_files = {
    "lemma": os.path.abspath(os.path.join(current_dir, "..", "lemmatized_sentences.csv")),
    "stem": os.path.abspath(os.path.join(current_dir, "..", "stemmed_sentences.csv"))
}

columns = {
    "lemma": "Lemmatized",
    "stem": "Stemmed"
}

# === Parametre kombinasyonları ===
data_types = ["lemma", "stem"]
architectures = {"CBOW": 0, "SkipGram": 1}
windows = [4, 10]
dimensions = [300, 1000]

# === Eğitim döngüsü ===
for data_type in data_types:
    file_path = data_files[data_type]
    column = columns[data_type]
    
    df = pd.read_csv(file_path)
    sentences = df[column].dropna().apply(lambda x: x.strip().split()).tolist()

    for arch_name, sg in architectures.items():
        for window in windows:
            for dimension in dimensions:
                # === Modeli eğit ===
                model = Word2Vec(
                    sentences=sentences,
                    vector_size=dimension,
                    window=window,
                    min_count=2,
                    workers=4,
                    sg=sg
                )

                # === Dosya isimleri ===
                model_name = f"word2vec_{data_type}_{arch_name.lower()}_w{window}_d{dimension}.model"
                vector_csv = f"vectors_{data_type}_{arch_name.lower()}_w{window}_d{dimension}.csv"
                
                # === Kaydet ===
                model.save(os.path.join(current_dir, model_name))

                vectors = []
                words = []

                for word in model.wv.index_to_key:
                    words.append(word)
                    vectors.append(model.wv[word])

                pd.DataFrame(vectors, index=words).to_csv(os.path.join(current_dir, vector_csv))

                print(f"✅ {model_name} ve {vector_csv} oluşturuldu.")
