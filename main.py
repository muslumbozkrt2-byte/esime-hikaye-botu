import os, requests, time, urllib.parse; from flask import Flask; from threading import Thread
app = Flask(''); app.route('/')(lambda: "Yapay Zeka Hikaye Fabrikasi Kesintisiz Aktif!")
def run_web_server(): port = int(os.environ.get("PORT", 8080)); app.run(host='0.0.0.0', port=port)
def whatsapp_link_firlat(gun):
    mesaj = f"🎬 Gunaydin Elif! Hikayemizin {gun}. Gun Bolumu Hazir.\n\nHemen en yuksek kalitede izlemek icin tikla: https://google.com"
    url = f"https://callmebot.com{urllib.parse.quote(mesaj)}&apikey=9302895"
    try: print(f"-> Bot Yanit Kodu: {requests.get(url, timeout=20).status_code}")
    except Exception as err: print(f"-> Hata: {err}")
def zamanlayici_dongusu():
    bolum_sayaci = 1; print("🚀 Sunucu uyaniyor... Ilk mesaj firlatiliyor..."); whatsapp_link_firlat(str(bolum_sayaci))
    while True:
        time.sleep(86400); bolum_sayaci += 1
        if bolum_sayaci > 10: print("🎉 10 gunluk seri tamamlandi!"); break
        whatsapp_link_firlat(str(bolum_sayaci))
if __name__ == "__main__": Thread(target=run_web_server).start(); zamanlayici_dongusu()
