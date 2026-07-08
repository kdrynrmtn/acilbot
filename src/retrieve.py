import sys
import os
sys.path.append(os.path.dirname(__file__))

import numpy as np
from sentence_transformers import SentenceTransformer
from database import tum_dokumanlari_getir

model = SentenceTransformer("intfloat/multilingual-e5-large")

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def ilgili_dokumanlari_bul(sorgu, top_k=2):

    sorgu_vec = model.encode(sorgu)
    
    dokumanlar = tum_dokumanlari_getir()
    
    benzerlikler = []
    for doc in dokumanlar:
        skor = cosine_similarity(sorgu_vec, doc["embedding"])
        benzerlikler.append((skor, doc))
    
    benzerlikler.sort(reverse=True)
    
    return benzerlikler[:top_k]

if __name__ == "__main__":
    sorgu = "Yanık tedavisi nasıl yapılır?"
    print(f"Sorgu: {sorgu}\n")
    
    sonuclar = ilgili_dokumanlari_bul(sorgu)
    
    print("En alakalı dokümanlar:")
    for skor, doc in sonuclar:
        print(f"\n  Benzerlik: {skor:.4f}")
        print(f"  Kaynak: {doc['source']}")
        print(f"  İçerik: {doc['content']}")