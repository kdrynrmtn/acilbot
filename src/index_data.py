import sys
import os
sys.path.append(os.path.dirname(__file__))

from sentence_transformers import SentenceTransformer
from database import tablo_olustur, dokuman_ekle, dokuman_sayisi

print("Model yükleniyor...")
model = SentenceTransformer("intfloat/multilingual-e5-large")
print("Model hazır!\n")

def dokumanlari_yukle():
    
    docs_klasoru = "docs"
    
    tablo_olustur()

    dosyalar = [f for f in os.listdir(docs_klasoru) if f.endswith(".txt")]
    
    if not dosyalar:
        print("docs/ klasöründe hiç .txt dosyası bulunamadı!")
        return
    
    print(f"{len(dosyalar)} dosya bulundu, yükleniyor...\n")
    
    for dosya_adi in dosyalar:
        dosya_yolu = os.path.join(docs_klasoru, dosya_adi)
        
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            icerik = f.read().strip()
        
        if not icerik:
            print(f"  ⚠ {dosya_adi} boş, atlandı")
            continue
        
        embedding = model.encode(icerik)
        
        dokuman_ekle(icerik, dosya_adi, embedding)
        print(f"  ✓ {dosya_adi} kaydedildi")
    
    print(f"\nToplam {dokuman_sayisi()} doküman veritabanında!")

if __name__ == "__main__":
    dokumanlari_yukle()