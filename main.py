import os, requests, time, urllib.parse; from flask import Flask; from threading import Thread; from datetime import datetime
app = Flask(''); app.route('/')(lambda: "Yapay Zeka Hikaye Fabrikasi Gulsen Icin Aktif!")
def run_web_server(): port = int(os.environ.get("PORT", 8080)); app.run(host='0.0.0.0', port=port)
WHATSAPP_NUMARASI = "905437171857"; CALLMEBOT_API_KEY = "9302895"
# 🔗 GÖNDERDİĞİNİZ GERÇEK GOOGLE DRIVE PAYLAŞIM LİNKİNİZ EKLENDİ:
ORTAK_IZLEME_LINKI = "https://drive.google.com/drive/folders/1PcEkXwAMhV1Le1trbnR8bRIplzvIm7BX"
def whatsapp_link_firlat(gun):
    mesaj = f"🎬 Gunaydin Gulsen! Hikayemizin {gun}. Gun Bolumu Hazir.\n\nHemen en yuksek kalitede izlemek icin tikla: {ORTAK_IZLEME_LINKI}"
    url = f"https://callmebot.com{WHATSAPP_NUMARASI}&text={urllib.parse.quote(mesaj)}&apikey={CALLMEBOT_API_KEY}"
    try: print(f"-> Bot Yanit Kodu: {requests.get(url, timeout=20).status_code}")
    except Exception as err: print(f"-> Hata: {err}")
def zamanlayici_dongusu():
    bolum_sayaci = 1; print("⏰ Zamanlayici bulutta baslatildi. Her gun saat 13:35 bekleniyor...")
    while True:
        turkiye_saati = (datetime.now().hour + 3) % 24; turkiye_dakikasi = datetime.now().minute
        if turkiye_saati == 13 and turkiye_dakikasi == 50:
            whatsapp_link_firlat(str(bolum_sayaci)); bolum_sayaci += 1
            if bolum_sayaci > 10: print("🎉 10 gunluk seri tamamlandi!"); break
            time.sleep(60)
        time.sleep(30)
if __name__ == "__main__": Thread(target=run_web_server).start(); zamanlayici_dongusu()
