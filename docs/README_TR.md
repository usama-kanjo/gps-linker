
<summary><strong>🇺🇸 English Version (Click to expand)</strong></summary>

# 📍 GPS Linker

**Fotoğraflardan GPS bilgilerini çıkarır ve 10+ harita servisi için anında linkler oluşturur!**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20WSL-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![ExifTool](https://img.shields.io/badge/Powered_by-ExifTool-orange.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

📸 **Akıllı** • 🗺️ **Hızlı** • 🎨 **Güzel**

</div>

## ✨ ÖZELLİKLER

| Özellik | Açıklama |
|---------|----------|
| 📍 **GPS Çıkarımı** | JPEG, HEIC, PNG, JPG formatlarından GPS koordinatlarını okur |
| 🌍 **Çoklu Harita** | Google Maps, OpenStreetMap, Yandex, Bing, Apple Maps ve daha fazlası |
| 🎨 **Renkli Çıktı** | Terminalde renkli ve emojili güzel görünüm |
| 🔄 **Toplu İşlem** | Tüm fotoğrafları tek komutla işleyin |
| 📋 **Çoklu Format** | Ondalık, DMS, JSON, KML formatlarında çıktı |
| 📱 **QR Kod** | Konum için QR kodu otomatik oluşturur |
| ⚡ **Hızlı Kurulum** | Tek komutla kurulum desteği |
| 🐧 **Çoklu Shell** | ZSH, Bash, Fish shell desteği |
| 🔧 **Symbolic Link** | Gelişmiş kurulum seçenekleri |

## 🚀 HIZLI KURULUM

### Tek Komutla Kurulum (En Kolay):
```bash
# Tek komutla her şeyi kur
bash -c "$(curl -fsSL https://raw.githubusercontent.com/UsamaKanjo/gps_linker/main/install.sh)"
```

### Manuel Kurulum:
```bash
# 1. Projeyi klonlayın
git clone https://github.com/UsamaKanjo/gps_linker.git
cd gps_linker

# 2. Kurulum script'ini çalıştırın
chmod +x install.sh
./install.sh

# 3. Kurulum sihirbazını takip edin
```

### Sadece Script İndirme:
```bash
# Script'i indirin
curl -O https://raw.githubusercontent.com/UsamaKanjo/gps_linker/main/gps_linker.py
chmod +x gps_linker.py

# Kullanın
./gps_linker.py fotoğraf.jpg
```

## 📖 KULLANIM

### Temel Kullanım:
```bash
# Tek bir fotoğraf için
gps_linker fotoğraf.jpg

# Etkileşimli mod (dizindeki fotoğrafları listeler)
gps_linker

# Yardım göster
gps_linker --help
```

### Gelişmiş Seçenekler:
```bash
# 📍 Sadece koordinatları göster
gps_linker -q fotoğraf.jpg

# 🔗 Sadece harita linklerini göster
gps_linker -l fotoğraf.jpg

# 🔄 Tüm JPG dosyalarını işle
gps_linker -b "*.jpg"

# 🗂️ Dizindeki tüm fotoğrafları işle
gps_linker -d /yol/fotoğraflar/

# 📊 JSON formatında çıktı
gps_linker -q --format=json fotoğraf.jpg

# 🌐 DMS formatında çıktı
gps_linker -q --format=dms fotoğraf.jpg
```

### Toplu İşlem Örnekleri:
```bash
# Tüm fotoğrafları işle
gps_linker --batch "*.jpg" "*.heic" "*.png"

# Sadece koordinatları CSV'ye çıkar
for img in *.jpg; do
    gps_linker -q "$img" >> coordinates.csv
done

# Sadece Google Maps linklerini al
gps_linker -l fotoğraf.jpg | grep "Google Maps"
```

## 🎯 KURULUM SEÇENEKLERİ

Kurulum script'i size 6 farklı seçenek sunar:

1. **Sistem Geneli** (`/usr/local/bin/`) - Tüm kullanıcılar için
2. **Sistem Geneli** (`/usr/bin/`) - Sistem geneli alternatif
3. **Kullanıcı Geneli** (`~/.local/bin/`) - Önerilen (sudo gerekmez)
4. **Kullanıcı Geneli** (`~/bin/`) - Alternatif kullanıcı dizini
5. **Özel Dizin** - Kendi belirlediğiniz dizin
6. **Mevcut Dizin** - Sadece bu dizinde kullan

## 📸 ÖRNEK ÇIKTI

```
========================================================================
                         📸 GPS Linker
========================================================================

📁 Dosya: ornek_fotoğraf.jpg
📁 Boyut: 2.14 MB
📁 Yol: /home/kullanici/fotoğraflar/ornek_fotoğraf.jpg

📍 Koordinat Bilgileri
────────────────────────────────────────────────────────────
📍 Enlem (Ondalık): 41.0082
📍 Boylam (Ondalık): 28.9784
📍 Enlem (DMS): 41°0'29.52" K
📍 Boylam (DMS): 28°58'42.24" D
⛰️ Yükseklik: 40.0 metre

🔗 Harita Linkleri
────────────────────────────────────────────────────────────
🌍 Google Maps: https://maps.google.com/?q=41.0082,28.9784
🛰️ Google Satellite: https://maps.google.com/?q=41.0082,28.9784&t=k
🗺️ OpenStreetMap: https://osm.org/?mlat=41.0082&mlon=28.9784
📍 Bing Maps: https://bing.com/maps?cp=41.0082~28.9784
📱 Apple Maps: https://maps.apple.com/?ll=41.0082,28.9784
🇹🇷 Yandex Haritalar: https://yandex.com.tr/harita/?pt=28.9784,41.0082
🔍 WikiMapia: https://wikimapia.org/#lang=tr&lat=41.0082&lon=28.9784

✅ İşlem tamamlandı!
```

## 🛠️ TEKNİK DETAYLAR

### Desteklenen Dosya Formatları:
- **JPEG/JPG** - Standart fotoğraf formatı
- **HEIC** - iPhone/iPad fotoğrafları
- **PNG** - Ekran görüntüleri ve diğer görseller

### Çıktı Formatları:
- **Ondalık Derece** - `41.0082,28.9784`
- **DMS** - `41°0'29.52" K 28°58'42.24" D`
- **JSON** - `{"lat": 41.0082, "lng": 28.9784, "alt": 40.0}`
- **KML** - Google Earth formatı
- **QR Kod** - Mobil cihazlarda hızlı erişim

### Harita Servisleri:
| Servis | Açıklama | İkon |
|--------|----------|------|
| Google Maps | Standart harita görünümü | 🌍 |
| Google Satellite | Uydu görüntüsü | 🛰️ |
| OpenStreetMap | Açık kaynak haritalar | 🗺️ |
| Bing Maps | Microsoft haritaları | 📍 |
| Apple Maps | iOS/macOS haritaları | 📱 |
| Yandex Haritalar | Türkiye ve Rusya için | 🇹🇷 |
| WikiMapia | Detaylı yer bilgileri | 🔍 |
| Google Earth | 3D görünüm | 🌎 |
| Yükseklik | Rakım bilgisi | ⛰️ |

## 🔧 GELİŞMİŞ YAPILANDIRMA

### Özel ZSH Konfigürasyonu:
Eğer ZSH konfigürasyonunuz özel bir dizindeyse (`~/.config/zsh` gibi), kurulum script'i otomatik olarak algılar ve PATH'i doğru dosyaya ekler.

### Alias Oluşturma:
```bash
# Manuel alias ekleme
echo "alias gps='python3 ~/.local/bin/gps_linker'" >> ~/.zshrc
source ~/.zshrc

# Kullanım
gps fotoğraf.jpg
```

### Otomasyon için:
```bash
# Tüm fotoğrafları işle ve JSON çıktısı al
gps_linker -b "*.jpg" --format=json > locations.json

# Sadece belirli koordinatları filtrele
gps_linker -b "*.heic" | grep "Enlem" | awk '{print $3}'
```

## 🐞 SIK SORULAN SORULAR

### ❓ GPS bilgisi bulunamıyor
**Çözüm:** Kamera ayarlarınızdan "Konum bilgisini kaydet" özelliğini açın.

### ❓ ExifTool bulunamadı
**Çözüm:**
```bash
# Ubuntu/Debian
sudo apt install libimage-exiftool-perl

# macOS
brew install exiftool

# Diğer dağıtımlar için README'ye bakın
```

### ❓ Komut bulunamadı (command not found)
**Çözüm:**
```bash
# PATH'i kontrol edin
echo $PATH

# Link'i kontrol edin
ls -la $(which gps_linker)

# Manuel çalıştırın
python3 /yol/gps_linker.py --help
```

### ❓ Renkler çalışmıyor
**Çözüm:** Terminalinizin renk desteğini kontrol edin veya `--color=always` kullanın.

## 📁 PROJE YAPISI

```
gps_linker/
├── gps_linker.py          # Ana uygulama
├── install.sh            # Akıllı kurulum script'i
├── README.md             # Bu dosya (Türkçe/English)
├── LICENSE               # MIT Lisansı
├── requirements.txt      # Python bağımlılıkları
├── examples/             # Kullanım örnekleri
│   ├── basic.sh         # Temel kullanım
│   ├── batch.sh         # Toplu işlem
│   └── automation.sh    # Otomasyon script'leri
└── tests/               # Test dosyaları
    └── test_gps.py      # Unit test'ler
```

## 🧪 TEST ETME

```bash
# Test fotoğrafları oluştur
python3 -c "from PIL import Image; Image.new('RGB', (100, 100)).save('test.jpg')"

# Script'i test et
gps_linker test.jpg

# Unit test'leri çalıştır
python3 -m pytest tests/
```

## 🤝 KATKI DAĞITMAK

Katkılarınızı memnuniyetle karşılıyoruz!

1. Fork yapın
2. Feature branch oluşturun: `git checkout -b feat/yeni-ozellik`
3. Değişikliklerinizi commit edin: `git commit -am 'Yeni özellik: ...'`
4. Branch'i push edin: `git push origin feat/yeni-ozellik`
5. Pull Request oluşturun

### Katkı Kuralları:
- Kod stilini koruyun (PEP 8)
- Yeni özellikler için test yazın
- README'yi güncelleyin
- Anlamlı commit mesajları kullanın

## 📝 LİSANS

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 GELİŞTİRİCİ

**Usama Kanjo**  
[![GitHub](https://img.shields.io/badge/GitHub-UsamaKanjo-black.svg)](https://github.com/UsamaKanjo)
[![Email](https://img.shields.io/badge/Email-m.osama.kanjo2007@gmail.com-blue.svg)](mailto:m.osama.kanjo2007@gmail.com)

## ⭐ DESTEK

Eğer bu projeyi beğendiyseniz:
- ⭐ GitHub'da yıldız verin
- 🐛 Issue açın
- 🔀 Fork yapın
- 📢 Sosyal medyada paylaşın

## 🔗 FAYDALI LİNKLER

- 📚 [ExifTool Dokümantasyonu](https://exiftool.org/)
- 🗺️ [Google Maps API](https://developers.google.com/maps)
- 🌐 [OpenStreetMap Wiki](https://wiki.openstreetmap.org/)
- 📖 [GPS Formatları](https://en.wikipedia.org/wiki/Geographic_coordinate_system)
- 💬 [Discord Topluluğu](https://discord.gg/örnek)

## 📊 İSTATİSTİKLER

![Kullanım İstatistikleri](https://img.shields.io/github/downloads/UsamaKanjo/gps_linker/total)
![Son Commit](https://img.shields.io/github/last-commit/UsamaKanjo/gps_linker)
![Issue Sayısı](https://img.shields.io/github/issues/UsamaKanjo/gps_linker)
![Pull Requests](https://img.shields.io/github/issues-pr/UsamaKanjo/gps_linker)

---

<div align="center">

### 🌟 "Her fotoğraf bir anı, her koordinat bir hikaye saklar" 🌟

**Kullanmaya başlayın ve fotoğraflarınızın gizemini çözün!**

[🚀 Hızlı Başlangıç](#-hızlı-kurulum) • [📖 Dokümantasyon](#-kullanım) • [🐛 Hata Bildir](https://github.com/UsamaKanjo/gps_linker/issues)

</div>

---

<details>
<summary><strong>🇺🇸 English Version (Click to expand)</strong></summary>

## 📍 GPS Linker

**Extracts GPS data from photos and creates instant links for 10+ map services!**

### Quick Start:
```bash
# One-line installation
bash -c "$(curl -fsSL https://raw.githubusercontent.com/UsamaKanjo/gps_linker/main/install.sh)"
```

### Features:
- 📍 GPS extraction from JPEG, HEIC, PNG
- 🌍 Multiple map services (Google, Apple, OpenStreetMap, etc.)
- 🎨 Colorful terminal output with emojis
- 🔄 Batch processing
- 📱 QR code generation
- ⚡ Fast and lightweight

[View full English documentation](docs/README_EN.md)

</details>
```

## Önemli Değişiklikler:

1. **Kullanıcı adınızı ekledim** - `UsamaKanjo`
2. **Tek komutlu kurulum** eklendi
3. **Kurulum seçenekleri** detaylandırıldı
4. **Gelişmiş yapılandırma** bölümü eklendi
5. **İngilizce versiyon** ekledim (expandable)
6. **İstatistik badge'leri** ekledim
7. **Test bölümü** ekledim
8. **Katkı kuralları** detaylandırıldı
9. **Daha profesyonel görünüm** için düzenlemeler
10. **Linkler** güncellendi

