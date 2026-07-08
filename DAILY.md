# AcilBot - Geliştirme Günlüğü

## Gün 1 - 29.06.2026
- RAG kavramını öğrendim (Retrieve, Augment, Generate)
- Proje konusunu belirledim: Offline Acil Durum Asistanı
- 15 test sorusu hazırladım

## Gün 2 - 30.06.2026
- Python venv kurulumu yaptım
- VS Code yapılandırdım
- Proje klasör yapısını oluşturdum (src/, data/, docs/)
- foundry-local-sdk kurulumu yaptım
- İlk main.py dosyasını yazdım

## Gün 3 - 01.07.2026
- Foundry Local CLI kurulumu yaptım
- phi-3.5-mini modelini indirdim
- Python kodu ile modele bağlandım
- İlk AI cevabını aldım!

## Gün 4 - 02.07.2026
- Proje modüler yapıya kavuştu (config.py, utils.py)
- .gitignore oluşturdum
- GitHub reposu açtım
- İlk temiz commit'i attım ve push ettim.

## Day 5 - 07.07.2026
- Embedding kavramını öğrendim (metin → sayı dizisi)
- sentence-transformers kütüphanesini kurdum
- cosine similarity ile vektör benzerliği hesapladım
- İngilizce model (all-MiniLM-L6-v2) Türkçe'de iyi çalışmadığını gördüm
- Türkçe için multilingual model (intfloat/multilingual-e5-large) deneme yanılma ile buldum
- "Yanık tedavisi" sorusuna doğru cevabı %87 benzerlikle bulan demo yazdım

## Day 6 - 08.07.2026
- SQLite nedir öğrendim (serverless, tek dosya veritabanı)
- database.py yazdım (bağlantı, tablo oluşturma, doküman ekleme fonksiyonları)
- 5 acil durum dokümanını embedding'leriyle birlikte veritabanına kaydettim
- data/acilbot.db dosyası oluştu
- Kullanıcı sorgularını anlamsal vektörlere dönüştüren ve   acilbot.db içerisindeki verilerle karşılaştırarak en alakalı dokümanları getiren (Retrieval) arama motoru mantığı sisteme entegre edildi