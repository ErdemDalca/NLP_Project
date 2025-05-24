import os
from gensim.models import Word2Vec

# === Ayarlar ===
current_dir = os.path.dirname(__file__)

data_types = ["lemma", "stem"]
architectures = ["cbow", "skipgram"]
windows = [4, 10]
dimensions = [300, 1000]

# === Sonuçları tut
results = []

# === Tüm model kombinasyonları üzerinde dön
for data_type in data_types:
    for arch in architectures:
        for window in windows:
            for dim in dimensions:
                model_name = f"word2vec_{data_type}_{arch}_w{window}_d{dim}.model"
                model_path = os.path.join(current_dir, model_name)
                
                if not os.path.exists(model_path):
                    print(f"⚠️ Model bulunamadı: {model_name}")
                    continue

                try:
                    model = Word2Vec.load(model_path)
                    if "game" in model.wv:
                        similar = model.wv.most_similar("game", topn=5)
                    else:
                        similar = [("Kelime bulunamadı", 0.0)]
                    
                    results.append((model_name, similar))
                except Exception as e:
                    print(f"❌ Hata ({model_name}): {e}")

# === Sonuçları yazdır
print("\n=== GAME Kelimesine En Benzer 5 Kelime ===\n")

for model_name, sim_words in results:
    print(f"📌 {model_name}")
    for word, score in sim_words:
        print(f"   → {word} ({score:.4f})")
    print()
