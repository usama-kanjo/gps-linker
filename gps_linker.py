#!/usr/bin/env python3
"""
GPS Linker - Fotoğraflardan GPS bilgilerini çıkarır ve harita linkleri oluşturur
"""

import subprocess
import sys
import os
import argparse
from typing import Optional, Dict, List
from pathlib import Path

# Renkli ve ikonlu çıktı için
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Icons:
    CAMERA = "📸"
    FILE = "📁"
    LOCATION = "📍"
    ALTITUDE = "⛰️"
    LINKS = "🔗"
    CLIPBOARD = "📋"
    EARTH = "🌍"
    SATELLITE = "🛰️"
    MAP = "🗺️"
    BING = "📍"
    APPLE = "📱"
    YANDEX = "🇹🇷"
    WARNING = "⚠️"
    ERROR = "❌"
    SUCCESS = "✅"
    SEARCH = "🔍"
    LIST = "📝"
    BATCH = "🔄"

def print_header(text: str):
    """Başlık yazdır"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.WHITE}{text:^60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")

def print_section(text: str, icon: str = ""):
    """Bölüm başlığı yazdır"""
    print(f"\n{Colors.BOLD}{Colors.PURPLE}{icon} {text}{Colors.END}")
    print(f"{Colors.PURPLE}{'─'*60}{Colors.END}")

def print_info(label: str, value: str, icon: str = ""):
    """Bilgi satırı yazdır"""
    print(f"{Colors.GREEN}{icon} {label}:{Colors.END} {Colors.WHITE}{value}{Colors.END}")

def print_link(name: str, url: str, icon: str = ""):
    """Link yazdır"""
    print(f"{Colors.YELLOW}{icon} {name}:{Colors.END}")
    print(f"  {Colors.BLUE}{url}{Colors.END}")

def get_gps_from_image(image_path: str) -> Optional[Dict[str, str]]:
    """Fotoğraftan GPS bilgilerini al"""
    try:
        result = subprocess.run(
            ['exiftool', '-GPSLatitude', '-GPSLongitude', '-GPSAltitude', 
             '-GPSLatitudeRef', '-GPSLongitudeRef', '-n', image_path],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        if result.returncode != 0:
            return None
        
        lines = result.stdout.strip().split('\n')
        gps_data = {}
        
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                gps_data[key.strip()] = value.strip()
        
        return gps_data if gps_data else None
        
    except FileNotFoundError:
        print(f"{Colors.RED}{Icons.ERROR} Hata: exiftool bulunamadı!{Colors.END}")
        print(f"{Colors.YELLOW}Kurulum için: sudo apt install libimage-exiftool-perl{Colors.END}")
        return None
    except Exception as e:
        print(f"{Colors.RED}{Icons.ERROR} Hata: {e}{Colors.END}")
        return None

def format_coordinate(value: str, coord_type: str = "lat") -> str:
    """Koordinatı daha okunabilir formata getir"""
    try:
        num = float(value)
        if coord_type == "lat":
            direction = "K" if num >= 0 else "G"
        else:
            direction = "D" if num >= 0 else "B"
        
        abs_num = abs(num)
        degrees = int(abs_num)
        minutes = int((abs_num - degrees) * 60)
        seconds = ((abs_num - degrees) * 60 - minutes) * 60
        
        return f"{degrees}°{minutes}'{seconds:.2f}\" {direction}"
    except:
        return value

def create_links(lat: float, lon: float, alt: Optional[float] = None) -> Dict[str, str]:
    """Çeşitli harita linkleri oluştur"""
    
    # Hassasiyeti ayarla (çok uzun ondalıklar için)
    lat_str = f"{lat:.8f}".rstrip('0').rstrip('.')
    lon_str = f"{lon:.8f}".rstrip('0').rstrip('.')
    
    links = {
        f"{Icons.EARTH} Google Maps": f"https://www.google.com/maps?q={lat_str},{lon_str}",
        f"{Icons.SATELLITE} Google Satellite": f"https://www.google.com/maps/@?api=1&map_action=map&basemap=satellite&zoom=18&center={lat_str},{lon_str}",
        f"{Icons.MAP} OpenStreetMap": f"https://www.openstreetmap.org/?mlat={lat_str}&mlon={lon_str}&zoom=17",
        f"{Icons.BING} Bing Maps": f"https://www.bing.com/maps?cp={lat_str}~{lon_str}&lvl=17",
        f"{Icons.APPLE} Apple Maps": f"https://maps.apple.com/?ll={lat_str},{lon_str}&z=17",
        f"{Icons.YANDEX} Yandex Haritalar": f"https://yandex.com.tr/harita/?pt={lon_str},{lat_str}&z=17&l=map",
        f"{Icons.SEARCH} WikiMapia": f"http://wikimapia.org/#lang=tr&lat={lat_str}&lon={lon_str}&z=18",
    }
    
    if alt:
        alt_str = str(int(alt)) if alt.is_integer() else f"{alt:.1f}"
        links[f"{Icons.ALTITUDE} Yükseklik"] = f"https://www.freemaptools.com/elevation-finder.htm?lat={lat_str}&lng={lon_str}"
        links[f"{Icons.EARTH} Google Earth 3D"] = f"https://earth.google.com/web/@{lat_str},{lon_str},{alt_str}a,1000d,35y,0h,0t,0r"
    
    return links

def process_image(image_path: str, args: argparse.Namespace) -> bool:
    """Tek bir fotoğrafı işle"""
    if not os.path.exists(image_path):
        print(f"{Colors.RED}{Icons.ERROR} Hata: '{image_path}' dosyası bulunamadı!{Colors.END}")
        return False
    
    file_size = os.path.getsize(image_path) / (1024*1024)  # MB cinsinden
    
    print_header(f"{Icons.CAMERA} GPS Linker")
    print_info("Dosya", os.path.basename(image_path), Icons.FILE)
    print_info("Boyut", f"{file_size:.2f} MB", Icons.FILE)
    print_info("Yol", os.path.abspath(image_path), Icons.FILE)
    
    gps_data = get_gps_from_image(image_path)
    
    if not gps_data:
        print_section(f"{Icons.WARNING} Uyarı", Icons.WARNING)
        print(f"{Colors.YELLOW}Bu dosyada GPS bilgisi bulunamadı.{Colors.END}")
        print(f"{Colors.YELLOW}Kamera ayarlarında 'Konumu kaydet' özelliğini açmayı deneyin.{Colors.END}")
        return False
    
    # Koordinatları al
    try:
        lat = float(gps_data.get('GPS Latitude', 0))
        lon = float(gps_data.get('GPS Longitude', 0))
        alt = gps_data.get('GPS Altitude')
        
        if alt:
            alt = float(alt)
    except ValueError:
        print(f"{Colors.RED}{Icons.ERROR} Hata: GPS koordinatları okunamadı!{Colors.END}")
        return False
    
    # Koordinat bilgileri
    print_section(f"{Icons.LOCATION} Koordinat Bilgileri", Icons.LOCATION)
    
    print_info("Enlem (Ondalık)", f"{lat:.8f}", Icons.LOCATION)
    print_info("Boylam (Ondalık)", f"{lon:.8f}", Icons.LOCATION)
    print_info("Enlem (DMS)", format_coordinate(str(lat), "lat"), Icons.LOCATION)
    print_info("Boylam (DMS)", format_coordinate(str(lon), "lon"), Icons.LOCATION)
    
    if alt:
        print_info("Yükseklik", f"{alt:.1f} metre", Icons.ALTITUDE)
    
    # Konum referansları
    lat_ref = gps_data.get('GPS Latitude Ref', 'North')
    lon_ref = gps_data.get('GPS Longitude Ref', 'East')
    print_info("Enlem Yönü", "Kuzey" if lat_ref.upper() in ['N', 'NORTH'] else "Güney", Icons.LOCATION)
    print_info("Boylam Yönü", "Doğu" if lon_ref.upper() in ['E', 'EAST'] else "Batı", Icons.LOCATION)
    
    # Harita linkleri
    print_section(f"{Icons.LINKS} Harita Linkleri", Icons.LINKS)
    
    links = create_links(lat, lon, alt)
    for name, url in links.items():
        print_link(name, url)
    
    # Kopyalama için
    print_section(f"{Icons.CLIPBOARD} Kopyalama İçin", Icons.CLIPBOARD)
    
    formats = [
        ("Ondalık", f"{lat:.8f},{lon:.8f}"),
        ("Google Maps Format", f"{lat},{lon}"),
        ("KML Formatı", f"<Point><coordinates>{lon},{lat},{alt if alt else 0}</coordinates></Point>"),
        ("JSON Format", f'{{"lat": {lat}, "lng": {lon}, "alt": {alt if alt else 0}}}'),
    ]
    
    for fmt_name, fmt_value in formats:
        print(f"{Colors.CYAN}◉ {fmt_name}:{Colors.END}")
        print(f"  {Colors.WHITE}{fmt_value}{Colors.END}")
    
    # QR kod linki
    print(f"\n{Colors.CYAN}📱 QR Kod:{Colors.END}")
    print(f"  {Colors.BLUE}https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://maps.google.com/?q={lat},{lon}{Colors.END}")
    
    print(f"\n{Colors.GREEN}{Icons.SUCCESS} İşlem tamamlandı!{Colors.END}")
    return True

def main():
    parser = argparse.ArgumentParser(
        description=f'{Icons.CAMERA} GPS Linker - Fotoğraflardan GPS bilgilerini çıkarır',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f'''
{Kullanım Örnekleri:}
  {Colors.CYAN}gps_linker fotoğraf.jpg{Colors.END}          - Tek fotoğraf işle
  {Colors.CYAN}gps_linker -l{Colors.END}                   - Sadece linkleri göster
  {Colors.CYAN}gps_linker -q{Colors.END}                   - Sadece koordinatları göster
  {Colors.CYAN}gps_linker -b "*.jpg"{Colors.END}           - Tüm JPG'leri işle
  {Colors.CYAN}gps_linker --help{Colors.END}               - Yardım mesajı
        '''
    )
    
    parser.add_argument('image', nargs='?', help='Fotoğraf dosyası yolu')
    parser.add_argument('-l', '--links-only', action='store_true', help='Sadece harita linklerini göster')
    parser.add_argument('-q', '--quiet', action='store_true', help='Sadece koordinatları göster (machine-readable)')
    parser.add_argument('-b', '--batch', help='Tüm dosyaları işle (ör: *.jpg, *.heic)')
    parser.add_argument('-d', '--directory', help='Belirtilen dizindeki tüm fotoğrafları işle')
    parser.add_argument('-f', '--format', choices=['decimal', 'dms', 'json'], default='decimal',
                       help='Koordinat çıktı formatı (varsayılan: decimal)')
    
    args = parser.parse_args()
    
    # Batch mod
    if args.batch:
        import glob
        files = glob.glob(args.batch)
        if not files:
            print(f"{Colors.YELLOW}{Icons.WARNING} Belirtilen pattern ile dosya bulunamadı: {args.batch}{Colors.END}")
            return
        
        print(f"{Colors.GREEN}{Icons.BATCH} Toplu işlem başlatılıyor: {len(files)} dosya{Colors.END}")
        success_count = 0
        
        for i, file in enumerate(files, 1):
            print(f"\n{Colors.CYAN}[{i}/{len(files)}]{Colors.END}")
            if process_image(file, args):
                success_count += 1
        
        print(f"\n{Colors.GREEN}{Icons.SUCCESS} Tamamlandı: {success_count}/{len(files)} dosya başarılı{Colors.END}")
        return
    
    # Directory mod
    if args.directory:
        if not os.path.isdir(args.directory):
            print(f"{Colors.RED}{Icons.ERROR} Hata: Dizin bulunamadı: {args.directory}{Colors.END}")
            return
        
        import glob
        extensions = ['*.jpg', '*.jpeg', '*.heic', '*.png', '*.JPG', '*.JPEG']
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(args.directory, ext)))
        
        if not files:
            print(f"{Colors.YELLOW}{Icons.WARNING} Dizinde fotoğraf bulunamadı: {args.directory}{Colors.END}")
            return
        
        print(f"{Colors.GREEN}{Icons.BATCH} Dizin işleniyor: {len(files)} dosya{Colors.END}")
        success_count = 0
        
        for i, file in enumerate(files, 1):
            print(f"\n{Colors.CYAN}[{i}/{len(files)}]{Colors.END}")
            if process_image(file, args):
                success_count += 1
        
        print(f"\n{Colors.GREEN}{Icons.SUCCESS} Tamamlandı: {success_count}/{len(files)} dosya başarılı{Colors.END}")
        return
    
    # Normal mod
    image_path = args.image
    
    if not image_path:
        # Mevcut dizindeki fotoğrafları listele
        files = [f for f in os.listdir('.') 
                if f.lower().endswith(('.jpg', '.jpeg', '.heic', '.png', '.JPG', '.JPEG'))]
        
        if not files:
            print(f"{Colors.YELLOW}{Icons.WARNING} Bulunduğunuz dizinde fotoğraf bulunamadı!{Colors.END}")
            image_path = input(f"{Colors.CYAN}📂 Fotoğraf yolunu girin: {Colors.END}").strip()
        else:
            print(f"\n{Colors.GREEN}{Icons.LIST} Mevcut fotoğraflar:{Colors.END}")
            for i, f in enumerate(files[:15], 1):
                size = os.path.getsize(f) / 1024  # KB cinsinden
                print(f"  {Colors.CYAN}{i:2}.{Colors.END} {f:<30} {Colors.YELLOW}({size:.1f} KB){Colors.END}")
            print(f"  {Colors.CYAN} 0.{Colors.END} Manuel yol gir")
            
            try:
                choice = int(input(f"\n{Colors.CYAN}🔢 Seçiminiz (1-{min(15, len(files))}): {Colors.END}"))
                if 1 <= choice <= len(files):
                    image_path = files[choice-1]
                else:
                    image_path = input(f"{Colors.CYAN}📂 Fotoğraf yolunu girin: {Colors.END}").strip()
            except:
                image_path = input(f"{Colors.CYAN}📂 Fotoğraf yolunu girin: {Colors.END}").strip()
    
    if args.quiet:
        gps_data = get_gps_from_image(image_path)
        if gps_data:
            lat = float(gps_data.get('GPS Latitude', 0))
            lon = float(gps_data.get('GPS Longitude', 0))
            
            if args.format == 'decimal':
                print(f"{lat:.8f},{lon:.8f}")
            elif args.format == 'dms':
                print(f"{format_coordinate(str(lat), 'lat')} {format_coordinate(str(lon), 'lon')}")
            elif args.format == 'json':
                alt = gps_data.get('GPS Altitude', 0)
                print(f'{{"lat": {lat}, "lng": {lon}, "alt": {alt}}}')
        return
    
    if args.links_only:
        gps_data = get_gps_from_image(image_path)
        if gps_data:
            lat = float(gps_data.get('GPS Latitude', 0))
            lon = float(gps_data.get('GPS Longitude', 0))
            alt = gps_data.get('GPS Altitude')
            alt = float(alt) if alt else None
            
            links = create_links(lat, lon, alt)
            for url in links.values():
                print(url)
        return
    
    # Normal işlem
    process_image(image_path, args)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}{Icons.WARNING} İşlem kullanıcı tarafından durduruldu.{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}{Icons.ERROR} Beklenmeyen hata: {e}{Colors.END}")
        sys.exit(1)
