# AcilBot - Yardımcı fonksiyonlar

def format_context(chunks):
    """Bulunan doküman parçalarını birleştirip LLM'e gönderilecek formata çevirir"""
    if not chunks:
        return "İlgili bilgi bulunamadı."
    
    context = ""
    for i, chunk in enumerate(chunks, 1):
        context += f"\n[Kaynak {i}]:\n{chunk}\n"
    
    return context

def print_separator():
    """Terminalde ayırıcı çizgi çizer"""
    print("-" * 50)