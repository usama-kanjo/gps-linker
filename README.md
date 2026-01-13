# 📍 GPS Linker

**Fotoğraflardan GPS bilgilerini çıkarır ve 10+ harita servisi için anında linkler oluşturur!**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20WSL-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![ExifTool](https://img.shields.io/badge/Powered_by-ExifTool-orange.svg)

📸 **Akıllı** • 🗺️ **Hızlı** • 🎨 **Güzel**

</div>

## ✨ ÖZELLİKLER

| Özellik | Açıklama |
|---------|----------|
| 📍 **GPS Çıkarımı** | JPEG, HEIC, PNG formatlarından GPS koordinatlarını okur |
| 🌍 **Çoklu Harita** | Google Maps, OpenStreetMap, Yandex, Bing ve daha fazlası |
| 🎨 **Renkli Çıktı** | Terminalde renkli ve ikonlu güzel görünüm |
| 🔄 **Toplu İşlem** | Tüm fotoğrafları tek komutla işleyin |
| 📋 **Çoklu Format** | Ondalık, DMS, JSON, KML formatlarında çıktı |
| 📱 **QR Kod** | Konum için QR kodu otomatik oluşturur |
| ⚡ **Hızlı** | Saniyeler içinde yüzlerce fotoğraf işler |

## 🚀 HIZLI KURULUM

### Gereksinimler:
```bash
# ExifTool kurulumu (Debian/Ubuntu)
sudo apt update
sudo apt install libimage-exiftool-perl python3

# ExifTool kurulumu (macOS)
brew install exiftool
```

### GPS Linker Kurulumu:
```bash
# 1. Script'i indirin
curl -O https://raw.githubusercontent.com/kullaniciadınız/gps-linker/main/gps_linker.py

# 2. Çalıştırılabilir yapın
chmod +x gps_linker.py

# 3. Global olarak erişilebilir yapın (isteğe bağlı)
sudo cp gps_linker.py /usr/local/bin/gps_linker

# 4. Symbolic link oluşturun (alternatif)
sudo ln -s $(pwd)/gps_linker.py /usr/local/bin/gps_linker
```

## 📖 KULLANIM

### Temel Kullanım:
```bash
# Tek bir fotoğraf için
gps_linker fotoğraf.jpg

# Veya
gps_linker IMG_2024.heic

# Veya
gps_linker DSC1234.png
```

### Gelişmiş Seçenekler:
```bash
# 📍 Sadece koordinatları göster
gps_linker -q fotoğraf.jpg
# Çıktı: 36.198228,37.090764

# 🔗 Sadece harita linklerini göster
gps_linker -l fotoğraf.jpg

# 🔄 Tüm JPG dosyalarını işle
gps_linker -b "*.jpg"

# 📂 Tüm HEIC dosyalarını işle
gps_linker -b "*.heic"

# 🗂️ Bir dizindeki tüm fotoğrafları işle
gps_linker -d /yol/fotoğraflar/

# 📊 Farklı formatlarda çıktı
gps_linker -q --format=json fotoğraf.jpg
# Çıktı: {"lat": 36.198228, "lng": 37.090764, "alt": 460.0}

gps_linker -q --format=dms fotoğraf.jpg
# Çıktı: 36°11'53.62" K 37°5'26.75" D
```

### Etkileşimli Mod:
```bash
# Mevcut dizindeki fotoğrafları listeler ve seçim yaptırır
gps_linker
```

## 📸 EKRAN GÖRÜNTÜSÜ

```
========================================================================
                         📸 GPS Linker
========================================================================

📁 Dosya: 20260113_221858.heic
📁 Boyut: 1.25 MB
📁 Yol: /home/user/fotoğraflar/20260113_221858.heic

────────────────────────────────────────────────────────────
📍 Koordinat Bilgileri
────────────────────────────────────────────────────────────
📍 Enlem (Ondalık): 36.19822840
📍 Boylam (Ondalık): 37.09076420
📍 Enlem (DMS): 36°11'53.62" K
📍 Boylam (DMS): 37°5'26.75" D
⛰️  Yükseklik: 460.0 metre
📍 Enlem Yönü: Kuzey
📍 Boylam Yönü: Doğu

────────────────────────────────────────────────────────────
🔗 Harita Linkleri
────────────────────────────────────────────────────────────
🌍 Google Maps:
  https://www.google.com/maps?q=36.1982284,37.0907642
🛰️ Google Satellite:
  https://www.google.com/maps/@?api=1&map_action=map&basemap=satellite&zoom=18&center=36.1982284,37.0907642
🗺️ OpenStreetMap:
  https://www.openstreetmap.org/?mlat=36.1982284&mlon=37.0907642&zoom=17
📍 Bing Maps:
  https://www.bing.com/maps?cp=36.1982284~37.0907642&lvl=17
📱 Apple Maps:
  https://maps.apple.com/?ll=36.1982284,37.0907642&z=17
🇹🇷 Yandex Haritalar:
  https://yandex.com.tr/harita/?pt=37.0907642,36.1982284&z=17&l=map
🔍 WikiMapia:
  http://wikimapia.org/#lang=tr&lat=36.1982284&lon=37.0907642&z=18
⛰️ Yükseklik:
  https://www.freemaptools.com/elevation-finder.htm?lat=36.1982284&lng=37.0907642
🌍 Google Earth 3D:
  https://earth.google.com/web/@36.1982284,37.0907642,460a,1000d,35y,0h,0t,0r

────────────────────────────────────────────────────────────
📋 Kopyalama İçin
────────────────────────────────────────────────────────────
◉ Ondalık:
  36.19822840,37.09076420
◉ Google Maps Format:
  36.1982284,37.0907642
◉ KML Formatı:
  <Point><coordinates>37.0907642,36.1982284,460.0</coordinates></Point>
◉ JSON Format:
  {"lat": 36.1982284, "lng": 37.0907642, "alt": 460.0}

📱 QR Kod:
  https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://maps.google.com/?q=36.1982284,37.0907642

✅ İşlem tamamlandı!
```

## 🔧 TEKNİK ÖZELLİKLER

### Desteklenen Formatlar:
- **📸 Fotoğraf:** JPEG, JPG, HEIC, PNG
- **📍 GPS Formatları:** Decimal, DMS (Derece/Dakika/Saniye)
- **📁 Çıktı Formatları:** Plain text, JSON, KML, Google Maps URL

### Desteklenen Harita Servisleri:
1. **Google Maps** - Standart harita görünümü
2. **Google Satellite** - Uydu görüntüsü
3. **OpenStreetMap** - Açık kaynak haritalar
4. **Bing Maps** - Microsoft haritaları
5. **Apple Maps** - iOS/MacOS haritaları
6. **Yandex Haritalar** - Rusya ve Türkiye için optimize
7. **WikiMapia** - Detaylı yer bilgileri
8. **Google Earth** - 3D görünüm
9. **Yükseklik Bulucu** - Rakım bilgisi

## 🐞 SIK KARŞILAŞILAN SORUNLAR

### "GPS bilgisi bulunamadı" hatası:
```bash
# Çözüm: Kamera ayarlarını kontrol edin
1. Kamera uygulamasını açın
2. Ayarlar (⚙️) bölümüne girin
3. "Konumu kaydet" veya "Coğrafi konum" seçeneğini açın
4. Telefon ayarlarından Kamera uygulamasına konum izni verin
```

### "exiftool bulunamadı" hatası:
```bash
# Debian/Ubuntu
sudo apt install libimage-exiftool-perl

# macOS
brew install exiftool

# Arch Linux
sudo pacman -S perl-image-exiftool

# Fedora
sudo dnf install perl-Image-ExifTool
```

### Renkler çalışmıyor:
```bash
# Terminal renk desteğini kontrol edin
echo $TERM

# Force color output
gps_linker --color=always fotoğraf.jpg
```

## 📁 PROJE YAPISI

```
gps-linker/
├── gps_linker.py          # Ana script
├── README.md             # Bu dosya
├── LICENSE              # MIT Lisansı
├── examples/            # Örnek kullanımlar
│   ├── basic_usage.sh   # Temel kullanım örnekleri
│   └── batch_processing.sh # Toplu işlem örnekleri
└── screenshots/         # Ekran görüntüleri
    └── example_output.png
```

## 🤝 KATKI DAĞITMAK

Katkılarınızı bekliyoruz! Katkıda bulunmak için:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📝 LİSANS

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 YAZAR

**Adınız** - [GitHub Profiliniz](https://github.com/kullaniciadınız)

## ⭐ DESTEK

Projeyi beğendiyseniz bir yıldız vermeyi unutmayın! ⭐

## 🔗 FAYDALI LİNKLER

- [ExifTool Resmi Sitesi](https://exiftool.org/)
- [Google Maps API](https://developers.google.com/maps)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [GPS Koordinat Formatları](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

---

<div align="center">
  
**"Her fotoğrafın bir hikayesi, her koordinatın bir macerası var"** ✨

</div>

## 📞 İLETİŞİM

Sorularınız veya önerileriniz için:
- GitHub Issues: [Yeni Issue Açın](https://github.com/kullaniciadınız/gps-linker/issues)
- E-posta: email@adresiniz.com

---

**Not:** Bu araç tamamen açık kaynak olup, gizliliğinize saygı duyar. Fotoğraflarınızı sunuculara yüklemez, tüm işlemler yerel bilgisayarınızda gerçekleşir.
