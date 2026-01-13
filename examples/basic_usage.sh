#!/bin/bash
# GPS Linker Temel Kullanım Örnekleri

echo "📸 GPS Linker Örnekleri"
echo "========================"

# 1. Temel kullanım
echo "1. Temel kullanım:"
echo "   gps_linker fotoğraf.jpg"
echo

# 2. Sadece linkler
echo "2. Sadece harita linkleri:"
echo "   gps_linker -l fotoğraf.jpg"
echo

# 3. Toplu işlem
echo "3. Tüm JPG'leri işle:"
echo "   gps_linker -b \"*.jpg\""
echo

# 4. Dizin işleme
echo "4. Bir dizindeki tüm fotoğraflar:"
echo "   gps_linker -d /yol/fotoğraflar/"
echo

# 5. JSON formatında çıktı
echo "5. JSON formatında çıktı:"
echo "   gps_linker -q --format=json fotoğraf.jpg"
