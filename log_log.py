import matplotlib.pyplot as plt
from collections import Counter

# Dosyayı oku
with open("tokenized_sentences.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Tüm kelimeleri al
words = text.split()

# Kelime frekanslarını hesapla
word_counts = Counter(words)

# Frekansları büyükten küçüğe sırala
frequencies = sorted(word_counts.values(), reverse=True)

# Log-log grafiğini çiz
plt.figure(figsize=(10, 6))
plt.loglog(range(1, len(frequencies) + 1), frequencies)
plt.title("Log-Log Grafiği (Zipf Dağılımı)")
plt.xlabel("Kelime sıralaması (rank)")
plt.ylabel("Kelime frekansı")
plt.grid(True, which="both", ls="--", lw=0.5)
plt.show()
