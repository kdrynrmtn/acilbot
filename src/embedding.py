import numpy as np
from sentence_transformers import SentenceTransformer

# Modeli yükle (ilk seferinde internetten indirir, sonra offline çalışır)
print("Model yükleniyor...")
model = SentenceTransformer("intfloat/multilingual-e5-large")
print("Model hazır!\n")

def cosine_similarity(vec1, vec2):
    """İki vektör arasındaki benzerliği hesaplar (0-1 arası)"""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Test cümleleri
sentences = [
    "Yanık durumunda bölgeye 15 dakika soğuk su uygulanmalıdır, buz veya krem sürülmemelidir.",
    "Kalp krizi şüphesinde hasta hemen dinlendirilmeli ve acil yardım çağrılmalıdır.",
    "Boğulma durumunda Heimlich manevrası uygulanarak hava yolu açılmalıdır.",
    "Kırık şüphesinde kemik hareket ettirilmemeli ve sabitlenmelidir.",
    "Elektrik çarpmasında önce elektriği kesin, sonra hastaya dokunun."
]

# Sorgu
query = "Yanık tedavisi nasıl yapılır?"

print(f"Sorgu: {query}\n")

# Tüm embedding'leri hesapla
query_vec = model.encode(query)
sentence_vecs = model.encode(sentences)

# Benzerlikleri hesapla ve göster
print("Benzerlik skorları:")
similarities = []
for i, sentence in enumerate(sentences):
    score = cosine_similarity(query_vec, sentence_vecs[i])
    similarities.append((score, sentence))
    print(f"  {score:.4f} → {sentence}")

# En benzer cümleyi bul
best = max(similarities)
print(f"\nEn benzer cümle: {best[1]}")
print(f"Benzerlik skoru: {best[0]:.4f}")