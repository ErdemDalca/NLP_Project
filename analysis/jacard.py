import os
import pandas as pd

# === Klasör yolu
csv_dir = "analysis/top5_outputs"

# === Model adı ve ilk 5 Match Index verilerini sakla
match_indices = {}

for fname in os.listdir(csv_dir):
    if fname.endswith(".csv") and fname.startswith("top5_"):
        model = fname.replace("top5_", "").replace(".csv", "")
        path = os.path.join(csv_dir, fname)
        df = pd.read_csv(path)

        # İlk satır giriş cümlesi, sonraki 5 satır önerilenler
        indices = df.iloc[1:6]["Match Index"].dropna().astype(int).tolist()
        match_indices[model] = set(indices)

# === Jaccard Matrisini oluştur
models = sorted(match_indices.keys())
matrix = []

for m1 in models:
    row = []
    for m2 in models:
        a = match_indices[m1]
        b = match_indices[m2]
        intersection = len(a & b)
        union = len(a | b)
        jaccard = round(intersection / union, 2) if union > 0 else 0.0
        row.append(jaccard)
    matrix.append(row)

# === DataFrame olarak kaydet
df_jaccard = pd.DataFrame(matrix, index=models, columns=models)
df_jaccard.to_csv("analysis/jaccard_matrix.csv")

print("✅ Jaccard matrisi oluşturuldu: analysis/jaccard_matrix.csv")
