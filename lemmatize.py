import csv
import nltk
from nltk.stem import WordNetLemmatizer

# Gerekli NLTK verileri
nltk.download('wordnet')
nltk.download('omw-1.4')

input_csv = "tokenized_sentences.csv"
output_csv = "lemmatized_sentences.csv"

lemmatizer = WordNetLemmatizer()
rows = []

# Tokenized CSV'yi oku ve lemmatize et
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        base = row["Base Sentence"]
        tokens = base.split()
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
        rows.append([row["Game"], base, " ".join(lemmas)])

# Yeni CSV'ye yaz
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Game", "Base Sentence", "Lemmatized"])
    writer.writerows(rows)

print(f"✅ Lemmatized veriler kaydedildi → {output_csv}")
