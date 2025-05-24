import csv
from nltk.stem import PorterStemmer

input_csv = "tokenized_sentences.csv"
output_csv = "stemmed_sentences.csv"

stemmer = PorterStemmer()
rows = []

# Tokenized CSV'yi oku ve stem işlemini uygula
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        base = row["Base Sentence"]
        tokens = base.split()
        stems = [stemmer.stem(token) for token in tokens]
        rows.append([row["Game"], base, " ".join(stems)])

# Yeni CSV'ye yaz
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Game", "Base Sentence", "Stemmed"])
    writer.writerows(rows)

print(f"✅ Stemmed veriler kaydedildi → {output_csv}")
