#!/bin/bash
# GPS Linker Kurulum Script'i

set -e

echo "📸 GPS Linker Kurulumu"
echo "======================"

# Renkler
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Hata mesajı fonksiyonu
error() {
    echo -e "${RED}❌ Hata: $1${NC}" >&2
    exit 1
}

# Başarı mesajı
success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# Uyarı mesajı
warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# ExifTool kontrolü
check_exiftool() {
    if command -v exiftool &> /dev/null; then
        success "ExifTool zaten kurulu"
    else
        warning "ExifTool bulunamadı"
        install_exiftool
    fi
}

# ExifTool kurulumu
install_exiftool() {
    echo "ExifTool kuruluyor..."
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Debian/Ubuntu
        if command -v apt-get &> /dev/null; then
            sudo apt-get update
            sudo apt-get install -y libimage-exiftool-perl
        # Arch
        elif command -v pacman &> /dev/null; then
            sudo pacman -S --noconfirm perl-image-exiftool
        # Fedora
        elif command -v dnf &> /dev/null; then
            sudo dnf install -y perl-Image-ExifTool
        else
            error "Desteklenmeyen Linux dağıtımı. Lütfen manuel olarak ExifTool kurun: https://exiftool.org/"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install exiftool
        else
            error "Homebrew bulunamadı. Lütfen Homebrew kurun veya ExifTool'u manuel yükleyin."
        fi
    else
        error "Desteklenmeyen işletim sistemi: $OSTYPE"
    fi
    
    success "ExifTool kuruldu"
}

# GPS Linker kurulumu
install_gps_linker() {
    echo "GPS Linker kuruluyor..."
    
    # Script'i indir
    if [[ ! -f "gps_linker.py" ]]; then
        if command -v curl &> /dev/null; then
            curl -O https://raw.githubusercontent.com/$GITHUB_USER/gps-linker/main/gps_linker.py
        elif command -v wget &> /dev/null; then
            wget https://raw.githubusercontent.com/$GITHUB_USER/gps-linker/main/gps_linker.py
        else
            error "curl veya wget bulunamadı"
        fi
    fi
    
    # Çalıştırılabilir yap
    chmod +x gps_linker.py
    
    # Global kurulum
    if [[ "$1" == "--global" ]]; then
        sudo cp gps_linker.py /usr/local/bin/gps_linker
        success "GPS Linker global olarak kuruldu (/usr/local/bin/gps_linker)"
    else
        # Local kurulum
        mkdir -p ~/bin
        cp gps_linker.py ~/bin/gps_linker
        chmod +x ~/bin/gps_linker
        
        # PATH kontrolü
        if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
            echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
            echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc 2>/dev/null || true
            warning "PATH'e ~/bin eklendi. Yeni terminal penceresi açın veya 'source ~/.bashrc' çalıştırın"
        fi
        
        success "GPS Linker local olarak kuruldu (~/bin/gps_linker)"
    fi
}

# Ana kurulum
main() {
    echo "Kurulum başlatılıyor..."
    
    # ExifTool kontrolü
    check_exiftool
    
    # GPS Linker kurulumu
    if [[ "$1" == "--global" ]]; then
        install_gps_linker --global
    else
        install_gps_linker
    fi
    
    # Test
    echo "Kurulum test ediliyor..."
    if command -v gps_linker &> /dev/null || [[ -f "/usr/local/bin/gps_linker" ]]; then
        success "GPS Linker başarıyla kuruldu!"
        echo
        echo "Kullanım:"
        echo "  gps_linker --help"
    else
        warning "GPS Linker kuruldu ama PATH'te bulunamıyor"
        echo "Manuel çalıştırmak için: ./gps_linker.py"
    fi
}

# GitHub kullanıcı adı (değiştirin)
GITHUB_USER="KULLANICI_ADINIZ"

# Ana fonksiyonu çalıştır
main "$@"
