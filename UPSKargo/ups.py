import requests

# Kullanıcıdan Tracking Number al
tracking_code = input("Lütfen kargo takip numarasını giriniz: ")

# Token almak için GET isteği yap
get_token = requests.get('http://localhost:3000')

# API için gerekli başlıklar
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.ship24.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.ship24.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-ship24-token': get_token.text.strip(),  # Token, localhost'tan alınan değer
}

# API isteği için JSON verisi
json_data = {
    'userAgent': '',
    'os': 'Windows',
    'browser': 'Chrome',
    'device': 'Unknown',
    'os_version': 'windows-10',
    'browser_version': '131.0.0.0',
    'deviceType': 'desktop',
    'orientation': 'landscape',
    'uL': 'tr-TR',
}

# API isteği
response = requests.post(
    f'https://api.ship24.com/api/parcels/{tracking_code}',
    headers=headers,
    json=json_data
)

# Yanıtın durum kodunu kontrol et (200 ve 201 başarı kabul edilir)
if response.status_code not in [200, 201]:
    print("API isteği başarısız oldu! Hata kodu:", response.status_code)
    exit()

# API yanıtını JSON formatına dönüştür
data = response.json()

# Yanıt içindeki gerekli alanları al
events = data.get("data", {}).get("events", [])  # Aşamalar (events)

# Eğer event'ler boşsa kullanıcıya bilgi ver
if not events:
    print("\nKargo Durumu: Bilgi bulunamadı.")
    exit()

# Aşama adlarını eşleştiren bir dictionary
milestone_names = {
    "Shipper created a label, UPS has not received the package yet.": "Etiket Oluşturuldu",
    "Pickup Scan": "Paketiniz Bizde",
    "Your package is on the way": "Yolda",
    "Warehouse Scan": "Depoda",
    "Out For Delivery": "Teslimat İçin Yola Çıktı",
    "Delivery": "Teslimat"
}

# Kargo aşamaları için çıktı oluştur
print("\nKargo Durumu:")
print("-" * 40)

for event in events:
    # Gerekli bilgileri al
    status = event.get("status", "")
    date_time = event.get("datetime", "")
    location = event.get("location", "Konum belirtilmemiş")
    
    # Aşama adını eşleştir
    name = milestone_names.get(status, "Bilinmeyen Aşama")
    
    # Eğer aşama "Bilinmeyen Aşama" ise atla
    if name == "Bilinmeyen Aşama":
        continue
    
    # Aşama bilgilerini yazdır
    print(f"Aşama: {name}")
    print(f"Durum: {status}")
    print(f"Tarih ve Saat: {date_time}")
    print(f"Konum: {location}")
    print("-" * 40)
