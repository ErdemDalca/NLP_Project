import csv
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Gerekli nltk verileri
nltk.download('wordnet')
nltk.download('omw-1.4')

# Dosya yolları
input_file = "tokenized_sentences.txt"
output_csv = "processed_sentences.csv"

# Araçlar
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Tüm cümleleri oku
with open(input_file, "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f.readlines() if line.strip()]

tokenized_corpus_lemmatized = []
tokenized_corpus_stemmed = []

for sentence in sentences:
    tokens = sentence.split()
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    stemmed = [stemmer.stem(token) for token in tokens]
    tokenized_corpus_lemmatized.append(lemmatized)
    tokenized_corpus_stemmed.append(stemmed)

# CSV'ye kaydet (her satırda Base, Lemmatized, Stemmed cümle)
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Base Sentence", "Lemmatized", "Stemmed"])  # başlık

    for base, lemmas, stems in zip(sentences, tokenized_corpus_lemmatized, tokenized_corpus_stemmed):
        writer.writerow([base, ' '.join(lemmas), ' '.join(stems)])

# İlk 5 cümleyi göster
for i in range(min(5, len(sentences))):
    print(f"Cümle {i+1} - Base: {sentences[i]}")
    print(f"Cümle {i+1} - Lemmatized: {tokenized_corpus_lemmatized[i]}")
    print(f"Cümle {i+1} - Stemmed: {tokenized_corpus_stemmed[i]}")
    print("\n")
