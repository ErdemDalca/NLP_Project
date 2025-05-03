import os
from gensim.models import Word2Vec

# === Ayarlar ===
model_dir = os.path.dirname(__file__)  # bu script ile aynı klasör
target_word = "game"

# === Tüm .model dosyalarını bul
model_files = [f for f in os.listdir(model_dir) if f.endswith(".model")]

print(f"🔍 Bulunan modeller: {len(model_files)}\n")

for model_file in sorted(model_files):
    model_path = os.path.join(model_dir, model_file)
    try:
        model = Word2Vec.load(model_path)
        print(f"📁 {model_file}")
        if target_word in model.wv:
            similar_words = model.wv.most_similar(target_word, topn=5)
            for word, score in similar_words:
                print(f"   - {word} ({score:.4f})")
        else:
            print(f"   ❌ '{target_word}' kelimesi bu modelde bulunamadı.")
    except Exception as e:
        print(f"   ⚠️ HATA: {e}")

    print("-" * 50)
