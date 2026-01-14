# 📍 GPS Linker

**Extracts GPS data from photos and creates instant links for 10+ map services!**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20WSL-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![ExifTool](https://img.shields.io/badge/Powered_by-ExifTool-orange.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

📸 **Smart** • 🗺️ **Fast** • 🎨 **Beautiful**

</div>

## ✨ FEATURES

| Feature | Description |
|---------|-------------|
| 📍 **GPS Extraction** | Reads GPS coordinates from JPEG, HEIC, PNG, JPG formats |
| 🌍 **Multiple Maps** | Google Maps, OpenStreetMap, Yandex, Bing, Apple Maps and more |
| 🎨 **Colorful Output** | Beautiful colored and emoji-rich terminal display |
| 🔄 **Batch Processing** | Process all photos with a single command |
| 📋 **Multiple Formats** | Output in Decimal, DMS, JSON, KML formats |
| 📱 **QR Code** | Automatically generates QR code for location |
| ⚡ **Quick Installation** | One-command installation support |
| 🐧 **Multi-Shell** | ZSH, Bash, Fish shell support |
| 🔧 **Symbolic Link** | Advanced installation options |

## 🚀 QUICK INSTALLATION

### One-Command Installation (Easiest):
```bash
# Install everything with one command
bash -c "$(curl -fsSL https://raw.githubusercontent.com/UsamaKanjo/gps_linker/main/install.sh)"
```

### Manual Installation:
```bash
# 1. Clone the project
git clone https://github.com/UsamaKanjo/gps_linker.git
cd gps_linker

# 2. Run the installation script
chmod +x install.sh
./install.sh

# 3. Follow the installation wizard
```

### Script Only:
```bash
# Download the script
curl -O https://raw.githubusercontent.com/UsamaKanjo/gps_linker/main/gps_linker.py
chmod +x gps_linker.py

# Use it
./gps_linker.py photo.jpg
```

## 📖 USAGE

### Basic Usage:
```bash
# For a single photo
gps_linker photo.jpg

# Interactive mode (lists photos in directory)
gps_linker

# Show help
gps_linker --help
```

### Advanced Options:
```bash
# 📍 Show only coordinates
gps_linker -q photo.jpg

# 🔗 Show only map links
gps_linker -l photo.jpg

# 🔄 Process all JPG files
gps_linker -b "*.jpg"

# 🗂️ Process all photos in directory
gps_linker -d /path/to/photos/

# 📊 Output in JSON format
gps_linker -q --format=json photo.jpg

# 🌐 Output in DMS format
gps_linker -q --format=dms photo.jpg
```

### Batch Processing Examples:
```bash
# Process all photos
gps_linker --batch "*.jpg" "*.heic" "*.png"

# Extract only coordinates to CSV
for img in *.jpg; do
    gps_linker -q "$img" >> coordinates.csv
done

# Get only Google Maps links
gps_linker -l photo.jpg | grep "Google Maps"
```

## 🎯 INSTALLATION OPTIONS

The installation script offers 6 different options:

1. **System-wide** (`/usr/local/bin/`) - For all users
2. **System-wide** (`/usr/bin/`) - Alternative system location
3. **User-wide** (`~/.local/bin/`) - Recommended (no sudo required)
4. **User-wide** (`~/bin/`) - Alternative user directory
5. **Custom Directory** - Your own specified directory
6. **Current Directory** - Use only in this directory

## 📸 EXAMPLE OUTPUT

```
========================================================================
                         📸 GPS Linker
========================================================================

📁 File: example_photo.jpg
📁 Size: 2.14 MB
📁 Path: /home/user/photos/example_photo.jpg

📍 Coordinate Information
────────────────────────────────────────────────────────────
📍 Latitude (Decimal): 41.0082
📍 Longitude (Decimal): 28.9784
📍 Latitude (DMS): 41°0'29.52" N
📍 Longitude (DMS): 28°58'42.24" E
⛰️ Altitude: 40.0 meters

🔗 Map Links
────────────────────────────────────────────────────────────
🌍 Google Maps: https://maps.google.com/?q=41.0082,28.9784
🛰️ Google Satellite: https://maps.google.com/?q=41.0082,28.9784&t=k
🗺️ OpenStreetMap: https://osm.org/?mlat=41.0082&mlon=28.9784
📍 Bing Maps: https://bing.com/maps?cp=41.0082~28.9784
📱 Apple Maps: https://maps.apple.com/?ll=41.0082,28.9784
🇹🇷 Yandex Maps: https://yandex.com.tr/harita/?pt=28.9784,41.0082
🔍 WikiMapia: https://wikimapia.org/#lang=en&lat=41.0082&lon=28.9784

✅ Process completed!
```

## 🛠️ TECHNICAL DETAILS

### Supported File Formats:
- **JPEG/JPG** - Standard photo format
- **HEIC** - iPhone/iPad photos
- **PNG** - Screenshots and other images

### Output Formats:
- **Decimal Degrees** - `41.0082,28.9784`
- **DMS** - `41°0'29.52" N 28°58'42.24" E`
- **JSON** - `{"lat": 41.0082, "lng": 28.9784, "alt": 40.0}`
- **KML** - Google Earth format
- **QR Code** - Quick access on mobile devices

### Map Services:
| Service | Description | Icon |
|---------|-------------|------|
| Google Maps | Standard map view | 🌍 |
| Google Satellite | Satellite imagery | 🛰️ |
| OpenStreetMap | Open source maps | 🗺️ |
| Bing Maps | Microsoft maps | 📍 |
| Apple Maps | iOS/macOS maps | 📱 |
| Yandex Maps | Optimized for Turkey and Russia | 🇹🇷 |
| WikiMapia | Detailed place information | 🔍 |
| Google Earth | 3D view | 🌎 |
| Elevation | Altitude information | ⛰️ |

## 🔧 ADVANCED CONFIGURATION

### Custom ZSH Configuration:
If your ZSH configuration is in a custom directory (like `~/.config/zsh`), the installation script automatically detects it and adds PATH to the correct file.

### Creating Aliases:
```bash
# Manual alias addition
echo "alias gps='python3 ~/.local/bin/gps_linker'" >> ~/.zshrc
source ~/.zshrc

# Usage
gps photo.jpg
```

### For Automation:
```bash
# Process all photos and get JSON output
gps_linker -b "*.jpg" --format=json > locations.json

# Filter only specific coordinates
gps_linker -b "*.heic" | grep "Latitude" | awk '{print $3}'
```

## 🐞 FREQUENTLY ASKED QUESTIONS

### ❓ GPS information not found
**Solution:** Enable "Save location information" in your camera settings.

### ❓ ExifTool not found
**Solution:**
```bash
# Ubuntu/Debian
sudo apt install libimage-exiftool-perl

# macOS
brew install exiftool

# Check README for other distributions
```

### ❓ Command not found
**Solution:**
```bash
# Check PATH
echo $PATH

# Check the link
ls -la $(which gps_linker)

# Run manually
python3 /path/to/gps_linker.py --help
```

### ❓ Colors not working
**Solution:** Check your terminal's color support or use `--color=always`.

## 📁 PROJECT STRUCTURE

```
gps_linker/
├── gps_linker.py          # Main application
├── install.sh            # Smart installation script
├── README.md             # This file (Turkish)
├── README_EN.md          # English documentation
├── LICENSE               # MIT License
├── requirements.txt      # Python dependencies
├── examples/             # Usage examples
│   ├── basic.sh         # Basic usage
│   ├── batch.sh         # Batch processing
│   └── automation.sh    # Automation scripts
└── tests/               # Test files
    └── test_gps.py      # Unit tests
```

## 🧪 TESTING

```bash
# Create test photos
python3 -c "from PIL import Image; Image.new('RGB', (100, 100)).save('test.jpg')"

# Test the script
gps_linker test.jpg

# Run unit tests
python3 -m pytest tests/
```

## 🤝 CONTRIBUTING

We welcome your contributions!

1. Fork the repository
2. Create feature branch: `git checkout -b feat/new-feature`
3. Commit your changes: `git commit -am 'Add new feature: ...'`
4. Push branch: `git push origin feat/new-feature`
5. Create Pull Request

### Contribution Guidelines:
- Maintain code style (PEP 8)
- Write tests for new features
- Update README
- Use meaningful commit messages

## 📝 LICENSE

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## 👨‍💻 DEVELOPER

**Usama Kanjo**  
[![GitHub](https://img.shields.io/badge/GitHub-UsamaKanjo-black.svg)](https://github.com/UsamaKanjo)
[![Email](https://img.shields.io/badge/Email-m.osama.kanjo2007@gmail.com-blue.svg)](mailto:m.osama.kanjo2007@gmail.com)

## ⭐ SUPPORT

If you like this project:
- ⭐ Give it a star on GitHub
- 🐛 Open an issue
- 🔀 Fork it
- 📢 Share on social media

## 🔗 USEFUL LINKS

- 📚 [ExifTool Documentation](https://exiftool.org/)
- 🗺️ [Google Maps API](https://developers.google.com/maps)
- 🌐 [OpenStreetMap Wiki](https://wiki.openstreetmap.org/)
- 📖 [GPS Formats](https://en.wikipedia.org/wiki/Geographic_coordinate_system)
- 💬 [Discord Community](https://discord.gg/example)

## 📊 STATISTICS

![Downloads](https://img.shields.io/github/downloads/UsamaKanjo/gps_linker/total)
![Last Commit](https://img.shields.io/github/last-commit/UsamaKanjo/gps_linker)
![Issues](https://img.shields.io/github/issues/UsamaKanjo/gps_linker)
![Pull Requests](https://img.shields.io/github/issues-pr/UsamaKanjo/gps_linker)

---

<div align="center">

### 🌟 "Every photo holds a memory, every coordinate tells a story" 🌟

**Start using it and uncover the mysteries of your photos!**

[🚀 Quick Start](#-quick-installation) • [📖 Documentation](#-usage) • [🐛 Report Bug](https://github.com/UsamaKanjo/gps_linker/issues)

</div>

---

<details>
<summary><strong>🇹🇷 Türkçe Versiyon (Genişletmek için tıklayın)</strong></summary>

## 📍 GPS Linker

**Fotoğraflardan GPS bilgilerini çıkarır ve 10+ harita servisi için anında linkler oluşturur!**

### Hızlı Başlangıç:
```bash
# Tek komutla kurulum
bash -c "$(curl -fsSL https://raw.githubusercontent.com/UsamaKanjo/gps_linker/main/install.sh)"
```

### Özellikler:
- 📍 JPEG, HEIC, PNG'den GPS çıkarımı
- 🌍 Çoklu harita servisleri (Google, Apple, OpenStreetMap vb.)
- 🎨 Renkli terminal çıktısı ve emojiler
- 🔄 Toplu işleme
- 📱 QR kodu oluşturma
- ⚡ Hızlı ve hafif


