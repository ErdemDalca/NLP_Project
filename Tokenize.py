import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from langdetect import detect

# nltk modüllerini indir
nltk.download('punkt')
nltk.download('stopwords')

# === Ayarlar ===
dataset_dir = "gdd_md_all"   # Ana klasör ismi
output_file = "tokenized_corpus.txt"  # Kaydedilecek dosya ismi

# İngilizce stopwords seti
stop_words = set(stopwords.words('english'))

# === Metin temizleme ve tokenizasyon fonksiyonu ===
def preprocess_text(text):
    text = text.lower()  # Küçük harfe çevir
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # linkleri kaldır
    text = re.sub(r'[^a-z.\s]', '', text)  # sadece harf, boşluk ve nokta bırak

    sentences = sent_tokenize(text)  # cümlelere ayır
    cleaned_sentences = []

    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tokens = [word for word in tokens if word not in stop_words and word.isalpha()]  # stopwords + sayı temizliği
        cleaned_sentences.append(" ".join(tokens))  # kelimeleri geri birleştir

    return cleaned_sentences  # her biri temizlenmiş bir cümle

# === Tüm dosyaları işleyelim ===
all_sentences = []

for root, dirs, files in os.walk(dataset_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Dil tespiti
                if detect(content) != "en":
                    print(f"Atlandı (İngilizce değil): {filepath}")
                    continue

                sentences = preprocess_text(content)
                all_sentences.extend(sentences)

            except Exception as e:
                print(f"Hata ({filepath}): {e}")

# === Sonucu satır satır kaydet ===
with open(output_file, "w", encoding="utf-8") as f:
    for sentence in all_sentences:
        f.write(sentence + "\n")

print(f"\n✅ İşlem tamamlandı. {len(all_sentences)} temiz cümle kaydedildi.")
print(f"📄 Çıktı dosyası: {output_file}")
