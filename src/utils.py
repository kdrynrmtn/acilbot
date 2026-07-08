# AcilBot - Yardımcı fonksiyonlar

def format_context(chunks):
    if not chunks:
        return "İlgili bilgi bulunamadı."
    
    context = ""
    for i, chunk in enumerate(chunks, 1):
        context += f"\n[Kaynak {i}]:\n{chunk}\n"
    
    return context

def print_separator():
    print("-" * 50)