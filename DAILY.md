# AcilBot - Geliştirme Günlüğü

## Gün 1 
- RAG kavramını öğrendim (Retrieve, Augment, Generate)
- Proje konusunu belirledim: Offline Acil Durum Asistanı
- 15 test sorusu hazırladım

## Gün 2 
- Python venv kurulumu yaptım
- VS Code yapılandırdım
- Proje klasör yapısını oluşturdum (src/, data/, docs/)
- foundry-local-sdk kurulumu yaptım
- İlk main.py dosyasını yazdım

## Gün 3 
- Foundry Local CLI kurulumu yaptım
- phi-3.5-mini modelini indirdim
- Python kodu ile modele bağlandım
- İlk AI cevabını aldım!

## Gün 4
- Proje modüler yapıya kavuştu (config.py, utils.py)
- .gitignore oluşturdum
- GitHub reposu açtım
- İlk temiz commit'i attım ve push ettim.

## Day 5 
- Embedding kavramını öğrendim (metin → sayı dizisi)
- sentence-transformers kütüphanesini kurdum
- cosine similarity ile vektör benzerliği hesapladım
- İngilizce model (all-MiniLM-L6-v2) Türkçe'de iyi çalışmadığını gördüm
- Türkçe için multilingual model (intfloat/multilingual-e5-large) deneme yanılma ile buldum
- "Yanık tedavisi" sorusuna doğru cevabı %87 benzerlikle bulan demo yazdım

## Day 6 
- SQLite nedir öğrendim (serverless, tek dosya veritabanı)
- database.py yazdım (bağlantı, tablo oluşturma, doküman ekleme fonksiyonları)
- 5 acil durum dokümanını embedding'leriyle birlikte veritabanına kaydettim
- data/acilbot.db dosyası oluştu
- Kullanıcı sorgularını anlamsal vektörlere dönüştüren ve   acilbot.db içerisindeki verilerle karşılaştırarak en alakalı dokümanları getiren (Retrieval) arama motoru mantığı sisteme entegre edildi

## Day 7 
- Test dosyalarını sildim, projeyi temizledim
- Her acil durum konusu için ayrı .txt dosyaları oluşturdum (docs/ klasörü)
  - Yanik.txt, Kanama.txt, Kalp_krizi&CPR.txt, Bogulma.txt
  - Kirik_cikik.txt, Elektrik_carpmasi.txt, Alerjik_reaksiyon.txt
  - Bayilma.txt, Nobet_Epilepsi.txt, Zehirlenme.txt
  - Deprem.txt, Donma_Hipotermi.txt, Bocek_isirmasi.txt
- Verileri kod içine yazmak yerine .txt dosyalarından okuyan daha temiz bir mimari kurdum
- index_data.py yeniden yazıldı (docs/ klasörünü tarayıp SQLite'a kaydediyor)

## Day 8
- Tüm .txt dosyalarını güvenilir kaynaklardan (Kızılay, sağlık siteleri vb.) referans alarak doldurdum
- 13 gerçek acil durum dokümanı başarıyla veritabanına kaydedildi