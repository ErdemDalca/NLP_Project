import os
import re
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from langdetect import detect
from bs4 import BeautifulSoup

# Gerekli NLTK verilerini indir
nltk.download('punkt')
nltk.download('stopwords')

# === Ayarlar ===
dataset_dir = "gdd_md_all"                 # Ana klasör (her repo bir klasör)
output_csv = "tokenized_sentences.csv"     # Çıktı dosyası
stop_words = set(stopwords.words('english'))

# === HTML + metin temizleme ===
def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()              # HTML tagleri sil
    text = text.lower()                                               # Küçük harf
    text = re.sub(r'https?://\S+|www\.\S+', '', text)                 # Link temizliği
    text = re.sub(r'[^a-z0-9.\s]', '', text)                          # Harf, rakam, nokta, boşluk dışında her şeyi kaldır
    return text

# === Sonuçları tutacak liste ===
rows = []

# === Klasörleri gez, dosyaları işle ===
for root, dirs, files in os.walk(dataset_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # İngilizce kontrolü
                if detect(content) != "en":
                    continue

                # Temizle ve tokenize et
                cleaned = clean_text(content)
                sentences = sent_tokenize(cleaned)

                # Oyun adı = repo klasörü
                game_title = os.path.basename(root)

                for sentence in sentences:
                    tokens = word_tokenize(sentence)
                    filtered_tokens = [w for w in tokens if w not in stop_words]

                    # Tuşlar anlamlıysa koru (örnek: w, a, s, d, q, e)
                    if all(len(w) == 1 for w in filtered_tokens):
                        keep = filtered_tokens
                    else:
                        keep = [w for w in filtered_tokens if len(w) > 1 or w in {'w', 'a', 's', 'd', 'e', 'q'}]

                    if not keep:
                        continue

                    base_sentence = " ".join(keep)
                    rows.append([game_title, base_sentence])

            except Exception as e:
                print(f"❌ Hata ({filepath}): {e}")

# === CSV dosyasına yaz ===
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Game", "Base Sentence"])
    writer.writerows(rows)

print(f"✅ Toplam {len(rows)} cümle işlendi → {output_csv}")
