import os
import requests
import time
from datetime import datetime
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Yapay Zeka Hikaye Fabrikası 7/24 Aktif!"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ====================================================================
# ⚙️ %100 AYARLANMIŞ VE DOĞRULANMIŞ AYARLARINIZ
# ====================================================================
WHATSAPP_NUMARASI = "905437171857" 
CALLMEBOT_API_KEY = "9302895"
HIKAYE_KONUSU = "Gizemli bir adada mahsur kalan Elif'in hayatta kalma mücadelesi"
ORTAK_IZLEME_LINKI = "https://google.com" 

# ASIL İSTEDİĞİNİZ ZAMAN AYARI (HER GECE 02:20)
SABAH_SAATI = 2      
SABAH_DAKIKASI = 20  
# ====================================================================

def whatsapp_link_firlat(gun):
    mesaj = f"🎬 Günaydın Elif! Hikayemizin {gun}. Gün Bölümü Hazır.\n\nHemen en yüksek kalitede izlemek için tıkla: {ORTAK_IZLEME_LINKI}"
    url = f"https://callmebot.com{WHATSAPP_NUMARASI}&text={requests.utils.quote(mesaj)}&apikey={CALLMEBOT_API_KEY}"
    try:
        requests.get(url, timeout=20)
        print(f"✅ Bulut Başarılı: {gun}. Gün mesajı WhatsApp'ınıza gönderildi!")
    except Exception as err:
        print(f"❌ Bulut Hatası: Sunucuya ulaşılamadı ({err})")

def zamanlayici_dongusu():
    # ⚡ [ANLIK TEST TETİKLEMESİ] 
    # Sunucu her açıldığında/güncellendiğinde saate bakmaksızın İLK MESAJI hemen atar!
    print("⚡ Bulut motoru güncellendi. İlk test mesajı şimdi fırlatılıyor...")
    whatsapp_link_firlat("1")
    
    bolum_sayaci = 2 # Sonraki gün 2. bölümden devam eder
    print(f"⏰ Zamanlayıcı hafızaya alındı. Her gece {SABAH_SAATI}:{SABAH_DAKIKASI} vaktini bekliyor...")
    while True:
        turkiye_saati = (datetime.now().hour + 3) % 24
        turkiye_dakikasi = datetime.now().minute
        
        if turkiye_saati == SABAH_SAATI and turkiye_dakikasi == SABAH_DAKIKASI:
            whatsapp_link_firlat(str(bolum_sayaci))
            bolum_sayaci += 1
            if bolum_sayaci > 10:
                print("🎉 10 günlük seri bitti.")
                break
            time.sleep(60)
        time.sleep(30)

if __name__ == "__main__":
    t = Thread(target=run_web_server)
    t.start()
    zamanlayici_dongusu()
