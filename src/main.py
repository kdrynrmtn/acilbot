import sys
import os
sys.path.append(os.path.dirname(__file__))

import openai
from config import MODEL_ID, BASE_URL, API_KEY
from utils import print_separator

def main():
    print_separator()
    print("AcilBot başlatılıyor...")
    print_separator()
    
    client = openai.OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    
    print("Modele soru soruluyor...")
    
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": "You are a helpful first aid assistant. Always respond in Turkish."},
            {"role": "user", "content": "Merhaba! Kendini tanıt."}
        ]
    )
    
    print_separator()
    print("Model cevabı:")
    print(response.choices[0].message.content)
    print_separator()

if __name__ == "__main__":
    main()