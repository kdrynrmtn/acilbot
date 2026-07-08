import sqlite3
import json
import os

VT_YOLU = "data/acilbot.db"

def baglanti_al():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(VT_YOLU)

def tablo_olustur():
    baglanti = baglanti_al()
    imlec = baglanti.cursor()

    imlec.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            source TEXT,
            embedding TEXT
        )
    """)

    baglanti.commit()
    baglanti.close()
    print("Veritabanı tablosu hazır!")

def dokuman_ekle(icerik, kaynak, gomme):
    baglanti = baglanti_al()
    imlec = baglanti.cursor()

    # Embedding'i JSON formatına çevir (liste → string)
    gomme_json = json.dumps(gomme.tolist())

    imlec.execute("""
        INSERT INTO documents (content, source, embedding)
        VALUES (?, ?, ?)
    """, (icerik, kaynak, gomme_json))

    baglanti.commit()
    baglanti.close()

def tum_dokumanlari_getir():
    baglanti = baglanti_al()
    imlec = baglanti.cursor()

    imlec.execute("SELECT id, content, source, embedding FROM documents")
    satirlar = imlec.fetchall()
    baglanti.close()

    dokumanlar = []
    for satir in satirlar:
        dokumanlar.append({
            "id": satir[0],
            "content": satir[1],
            "source": satir[2],
            "embedding": json.loads(satir[3])
        })

    return dokumanlar

def dokuman_sayisi():
    baglanti = baglanti_al()
    imlec = baglanti.cursor()
    imlec.execute("SELECT COUNT(*) FROM documents")
    sayi = imlec.fetchone()[0]
    baglanti.close()
    return sayi

if __name__ == "__main__":
    tablo_olustur()
    print(f"Toplam doküman sayısı: {dokuman_sayisi()}")