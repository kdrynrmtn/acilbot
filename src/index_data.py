from database import insert_document
from utils import model 
import os

data = [
    "Yanık durumunda bölgeye 15 dakika soğuk su uygulanmalıdır, buz veya krem sürülmemelidir.",
    "Kalp krizi şüphesinde hasta hemen dinlendirilmeli ve acil yardım çağrılmalıdır.",
    "Boğulma durumunda Heimlich manevrası uygulanarak hava yolu açılmalıdır.",
    "Kırık şüphesinde kemik hareket ettirilmemeli ve sabitlenmelidir.",
    "Elektrik çarpmasında önce elektriği kesin, sonra hastaya dokunun.",
    "Burun kanamasında baş hafifçe öne eğilmeli, burun kanatlarına baskı uygulanmalıdır.",
    "Arı sokmasında iğne varsa çıkarılmalı, bölgeye soğuk uygulama yapılmalıdır.",
    "Donma durumunda bölge yavaşça ısıtılmalı, doğrudan ateşle temas ettirilmemelidir."
]

def index_all():
    print("Veriler veritabanına işleniyor...")
    for sentence in data:
        embedding = model.encode(sentence)
        insert_document(sentence, embedding)
        print(f"Başarıyla eklendi: {sentence[:30]}...")

if __name__ == "__main__":
    index_all()
    print("\nTüm ilk yardım bilgileri hafızaya alındı!")