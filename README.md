# POYRAZ Yer Kontrol İstasyonu (YKI)
## Proje Hakkında
Bu proje, Teknofest Savaşan İHA Yarışması kapsamında verilen Yer Kontrol İstasyonu geliştirme görevi için hazırlanmıştır.

Uygulama, ArduPilot SITL simülasyonundan MAVLink protokolü üzerinden telemetri verilerini alarak kullanıcı arayüzünde göstermektedir.

## Kullanılan Teknolojiler
* Python 3.11
* PyQt5
* PyMAVLink
* Folium
* PyQtWebEngine
* Özellikler
* MAVLink bağlantısı
* Anlık telemetri takibi
* İrtifa görüntüleme
* Hız görüntüleme
* Uçuş modu görüntüleme
* Batarya durumu görüntüleme
* GPS koordinatlarının görüntülenmesi
* Harita üzerinde İHA konumunun gösterilmesi
* Çok iş parçacıklı (QThread) yapı ile kesintisiz arayüz
## Kurulum
Gerekli kütüphaneleri yüklemek için:
```text
pip install -r requirements.txt
```
## Çalıştırma
Öncelikle Mission Planner üzerinden ArduPilot SITL başlatılmalıdır.

Daha sonra proje dizininde:
```
python main.py
```
komutu çalıştırılarak uygulama başlatılır.

Proje Yapısı
```text
Poyraz_YKI/
│
├── main.py
├── requirements.txt
├── README.md
│
├── ui/
│   └── main_window.py
│
├── mavlink/
│   └── telemetry_worker.py
│
└── map/
    └── map_widget.py
```
