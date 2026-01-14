#!/bin/bash
# GPS Linker Kurulum Script'i - Symbolic Link Versiyonu

set -e

echo "📸 GPS Linker Kurulumu"
echo "======================"

# Renkler
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

error() { echo -e "${RED}❌ Hata: $1${NC}" >&2; exit 1; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }

# Symbolic link oluştur
create_symlink() {
    local target_path="$1"
    local link_name="$2"
    
    echo "Hedef: $target_path"
    echo "Link ismi: $link_name"
    echo ""
    
    # Mevcut linkleri kontrol et
    existing_links=()
    
    # Sistem genelinde gps_linker arat
    echo "Mevcut linkler aranıyor..."
    
    # /usr/local/bin kontrol
    if [[ -L "/usr/local/bin/$link_name" ]]; then
        existing_links+=("/usr/local/bin/$link_name -> $(readlink "/usr/local/bin/$link_name")")
    fi
    
    # /usr/bin kontrol
    if [[ -L "/usr/bin/$link_name" ]]; then
        existing_links+=("/usr/bin/$link_name -> $(readlink "/usr/bin/$link_name")")
    fi
    
    # ~/.local/bin kontrol
    if [[ -L "$HOME/.local/bin/$link_name" ]]; then
        existing_links+=("$HOME/.local/bin/$link_name -> $(readlink "$HOME/.local/bin/$link_name")")
    fi
    
    # ~/bin kontrol
    if [[ -L "$HOME/bin/$link_name" ]]; then
        existing_links+=("$HOME/bin/$link_name -> $(readlink "$HOME/bin/$link_name")")
    fi
    
    if [[ ${#existing_links[@]} -gt 0 ]]; then
        warning "Mevcut linkler bulundu:"
        for link in "${existing_links[@]}"; do
            echo "  $link"
        done
        
        read -p "Mevcut linkleri silmek istiyor musunuz? (e/h) [e]: " remove_old
        remove_old=${remove_old:-e}
        
        if [[ "$remove_old" == "e" ]]; then
            for link_path in "${existing_links[@]%% -> *}"; do
                if [[ -L "$link_path" ]]; then
                    rm "$link_path"
                    success "Silindi: $link_path"
                fi
            done
        fi
    fi
    
    # Kurulum seçenekleri
    echo ""
    echo "📌 Kurulum Seçenekleri:"
    echo "  1. Sistem geneli (sudo) - /usr/local/bin/"
    echo "  2. Sistem geneli (sudo) - /usr/bin/"
    echo "  3. Kullanıcı geneli - ~/.local/bin/"
    echo "  4. Kullanıcı geneli - ~/bin/"
    echo "  5. Özel dizin"
    echo "  6. Mevcut dizinde bırak"
    echo ""
    
    read -p "Seçiminiz (1-6) [3]: " choice
    choice=${choice:-3}
    
    case $choice in
        1)
            link_dir="/usr/local/bin"
            use_sudo=true
            ;;
        2)
            link_dir="/usr/bin"
            use_sudo=true
            ;;
        3)
            link_dir="$HOME/.local/bin"
            use_sudo=false
            ;;
        4)
            link_dir="$HOME/bin"
            use_sudo=false
            ;;
        5)
            read -p "Özel dizin yolu: " custom_dir
            link_dir="$custom_dir"
            use_sudo=false
            ;;
        6)
            echo ""
            echo "ℹ️  Script mevcut dizinde bırakıldı."
            echo "   Çalıştırmak için: ./gps_linker.py"
            return 0
            ;;
        *)
            link_dir="$HOME/.local/bin"
            use_sudo=false
            ;;
    esac
    
    # Dizin yoksa oluştur
    if [[ ! -d "$link_dir" ]]; then
        echo "Dizin oluşturuluyor: $link_dir"
        if [[ "$use_sudo" == true ]]; then
            sudo mkdir -p "$link_dir"
        else
            mkdir -p "$link_dir"
        fi
    fi
    
    # Link oluştur
    link_path="$link_dir/$link_name"
    
    if [[ "$use_sudo" == true ]]; then
        sudo ln -sf "$target_path" "$link_path"
        sudo chmod +x "$link_path"
    else
        ln -sf "$target_path" "$link_path"
        chmod +x "$link_path"
    fi
    
    success "Symbolic link oluşturuldu: $link_path → $target_path"
    
    # PATH kontrolü (sadece bilgi amaçlı)
    if [[ ":$PATH:" != *":$link_dir:"* ]]; then
        warning "NOT: $link_dir dizini PATH'te yoksa komut çalışmayabilir."
        echo "Mevcut PATH: $PATH"
        echo ""
        echo "PATH'e eklemek için:"
        
        # ZSH konfigürasyonunu bul
        zsh_config=""
        if [[ -n "$ZDOTDIR" ]] && [[ -f "$ZDOTDIR/.zshrc" ]]; then
            zsh_config="$ZDOTDIR/.zshrc"
        elif [[ -n "$ZSH_CUSTOM" ]] && [[ -f "$ZSH_CUSTOM/.zshrc" ]]; then
            zsh_config="$ZSH_CUSTOM/.zshrc"
        elif [[ -f "$HOME/.config/zsh/.zshrc" ]]; then
            zsh_config="$HOME/.config/zsh/.zshrc"
        elif [[ -f "$HOME/.zshrc" ]]; then
            zsh_config="$HOME/.zshrc"
        fi
        
        if [[ -n "$zsh_config" ]]; then
            echo "  echo 'export PATH=\"$link_dir:\$PATH\"' >> $zsh_config"
        fi
        
        if [[ -f "$HOME/.bashrc" ]]; then
            echo "  echo 'export PATH=\"$link_dir:\$PATH\"' >> ~/.bashrc"
        fi
        
        echo ""
        echo "Veya her seferinde manuel çalıştırın:"
        echo "  $link_path"
    else
        echo ""
        echo "🎉 Kurulum tamamlandı!"
        echo "Kullanım: $link_name --help"
    fi
}

# ExifTool kontrolü
check_exiftool() {
    if command -v exiftool &> /dev/null; then
        exiftool_version=$(exiftool -ver 2>/dev/null || echo "mevcut")
        success "ExifTool zaten kurulu ($exiftool_version)"
        return 0
    else
        warning "ExifTool bulunamadı"
        return 1
    fi
}

# Ana kurulum
main() {
    # Script dosyasını kontrol et
    script_name="gps_linker.py"
    
    if [[ ! -f "$script_name" ]]; then
        error "'$script_name' dosyası bulunamadı! Script ile aynı dizinde çalıştırın."
    fi
    
    # Çalıştırılabilir yap
    chmod +x "$script_name"
    
    echo "📄 Script: $(pwd)/$script_name"
    echo "📏 Boyut: $(du -h "$script_name" | cut -f1)"
    echo ""
    
    # ExifTool kontrolü
    if ! check_exiftool; then
        echo ""
        warning "GPS Linker çalışması için ExifTool gereklidir!"
        echo "Kurulum komutları:"
        echo "  Ubuntu/Debian: sudo apt install libimage-exiftool-perl"
        echo "  Arch: sudo pacman -S perl-image-exiftool"
        echo "  Fedora: sudo dnf install perl-Image-Exiftool"
        echo "  macOS: brew install exiftool"
        echo ""
        read -p "Devam etmek istiyor musunuz? (e/h) [e]: " continue_install
        continue_install=${continue_install:-e}
        
        if [[ "$continue_install" != "e" ]]; then
            echo "Kurulum iptal edildi."
            exit 0
        fi
    fi
    
    # Symbolic link oluştur
    create_symlink "$(pwd)/$script_name" "gps_linker"
    
    # Test et
    echo ""
    echo "🔍 Kurulum test ediliyor..."
    
    if command -v gps_linker &> /dev/null; then
        success "GPS Linker başarıyla kuruldu!"
        echo ""
        gps_linker --help | head -20
    else
        warning "GPS Linker PATH'te bulunamadı ama link oluşturuldu."
        echo ""
        echo "Manuel çalıştırma seçenekleri:"
        echo "  1. Tam yol ile: $(which gps_linker 2>/dev/null || echo "link_bulunamadı")"
        echo "  2. ./gps_linker.py ile mevcut dizinden"
        echo "  3. Link dizininden: [link_dizin_yolu]/gps_linker"
    fi
}

main "$@"
