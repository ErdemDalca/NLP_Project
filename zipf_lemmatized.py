import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

# === Çıktı klasörü ===
output_dir = "test_outputs"
os.makedirs(output_dir, exist_ok=True)

# === CSV'den lemmatized verileri al ===
df = pd.read_csv("processed_sentences.csv")
sentences = df["Lemmatized"].dropna().tolist()

# === Kelime frekansları ===
words = []
for sentence in sentences:
    tokens = sentence.split()
    words.extend([word for word in tokens if word.isalpha()])

word_freq = Counter(words)
sorted_freqs = sorted(word_freq.values(), reverse=True)

# === Log-log Zipf grafiği ===
plt.figure(figsize=(10, 6))
plt.loglog(range(1, len(sorted_freqs)+1), sorted_freqs)
plt.title("Zipf Log-Log Grafiği (Lemmatized Veriler)")
plt.xlabel("Kelime Sırası (r)")
plt.ylabel("Frekans (f)")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()

# === Kayıt ===
output_path = os.path.join(output_dir, "zipf_loglog_lemmatized.png")
plt.savefig(output_path)
plt.show()
