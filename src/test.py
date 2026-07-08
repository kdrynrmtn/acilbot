import sys
import os
sys.path.append(os.path.dirname(__file__))

import numpy as np
from sentence_transformers import SentenceTransformer
from database import tablo_olustur, dokuman_ekle, tum_dokumanlari_getir, dokuman_sayisi


print("Model yükleniyor...")
model = SentenceTransformer("intfloat/multilingual-e5-large")
print("Model hazır!\n")


documents = [
    {
        "content": "Yanık durumunda bölgeye 15 dakika soğuk su uygulanmalıdır. Buz veya krem sürülmemelidir. Geniş yanıklarda hasta hemen hastaneye götürülmelidir.",
        "source": "ilk_yardim_yanik.txt"
    },
    {
        "content": "Kalp krizi belirtileri: göğüs ağrısı, sol kola yayılan ağrı, nefes darlığı. Hasta dinlendirilmeli, 112 aranmalı ve aspirin verilmelidir.",
        "source": "ilk_yardim_kalp.txt"
    },
    {
        "content": "Boğulma durumunda Heimlich manevrası uygulanır. Kişinin arkasına geçilir, bel hizasında yumruk yapılır ve içe-yukarı doğru baskı uygulanır.",
        "source": "ilk_yardim_bogulma.txt"
    },
    {
        "content": "Kırık şüphesinde kemik kesinlikle hareket ettirilmemelidir. Kırık bölge sabitlenmeli, soğuk uygulama yapılmalı ve hasta hastaneye götürülmelidir.",
        "source": "ilk_yardim_kirik.txt"
    },
    {
        "content": "Elektrik çarpmasında önce elektrik kaynağı kesilmelidir. Hastaya çıplak elle dokunulmamalıdır. Hasta bilinci kapalıysa CPR uygulanmalıdır.",
        "source": "ilk_yardim_elektrik.txt"
    }
]


tablo_olustur()

print("Dokümanlar veritabanına kaydediliyor...")
for doc in documents:
    embedding = model.encode(doc["content"])
    dokuman_ekle(doc["content"], doc["source"], embedding)
    print(f"  ✓ {doc['source']} kaydedildi")


print(f"\nToplam doküman sayısı: {dokuman_sayisi()}")


print("\nVeritabanındaki dokümanlar:")
all_docs = tum_dokumanlari_getir()
for doc in all_docs:
    print(f"  ID: {doc['id']} | Kaynak: {doc['source']}")
    print(f"  İçerik: {doc['content'][:50]}...")
    print(f"  Embedding boyutu: {len(doc['embedding'])}")
    print()