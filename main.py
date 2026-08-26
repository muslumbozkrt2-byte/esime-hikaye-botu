import os
import requests
import time
from datetime import datetime
from flask import Flask
from threading import Thread

# --- BULUT SUNUCUSUNU UYANIK TUTMA SERVİSİ (FLASK) ---
app = Flask('')

@app.route('/')
def home():
    return "Yapay Zeka Hikaye Fabrikası 7/24 Aktif!"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- ⚙️ SABİTLENMİŞ AYARLARINIZ ---
WHATSAPP_NUMARASI = "905437171857" 
CALLMEBOT_API_KEY = "9302895"
ORTAK_IZLEME_LINKI = "https://google.com" # Drive klasör linkinizi daha sonra buraya yapıştırabilirsiniz

def whatsapp_link_firlat(gun):
    mesaj = f"🎬 Günaydın Elif! Hikayemizin {gun}. Gün Bölümü Hazır.\n\nHemen en yüksek kalitede izlemek için tıkla: {ORTAK_IZLEME_LINKI}"
    url = f"https://callmebot.com{WHATSAPP_NUMARASI}&text={requests.utils.quote(mesaj)}&apikey={CALLMEBOT_API_KEY}"
    try:
        requests.get(url, timeout=20)
        print(f"✅ Bulut Başarılı: {gun}. Gün mesajı WhatsApp'ınıza gönderildi!")
    except Exception as err:
        print(f"❌ Bulut Hatası: Sunucuya ulaşılamadı ({err})")

def zamanlayici_dongusu():
    bolum_sayaci = 1
    print("⏰ Gece 02:20 Bekçisi Bulutta Başlatıldı...")
    while True:
        # Sunucu saatini Türkiye saatine uyarlar (+3 saat farkı)
        turkiye_saati = (datetime.now().hour + 3) % 24
        turkiye_dakikasi = datetime.now().minute
        
        # ⏰ YENİ ZAMANLAYICI AYARI: HER GECE SAAT 02:20
        if turkiye_saati == 2 and turkiye_dakikasi == 20:
            whatsapp_link_firlat(str(bolum_sayaci))
            bolum_sayaci += 1
            if bolum_sayaci > 10:
                print("🎉 10 günlük seri bitti.")
                break
            time.sleep(60) # Aynı dakika içinde mükerrer gönderimi engeller
        time.sleep(30) # Saati kontrol periyodu

if __name__ == "__main__":
    t = Thread(target=run_web_server)
    t.start()
    zamanlayici_dongusu()
      
