#!/usr/bin/env python3
"""
GPS Linker - Kurulum dosyası
"""

from setuptools import setup, find_packages
import os
import re

# README'dan açıklamayı oku
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Version'ı dosyadan oku
def get_version():
    with open('gps_linker.py', 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", content)
        if match:
            return match.group(1)
    return '1.0.0'

setup(
    name='gps-linker',
    version=get_version(),
    
    # Meta veriler
    author='Adınız',
    author_email='email@adresiniz.com',
    description='Fotoğraflardan GPS bilgilerini çıkarır ve harita linkleri oluşturur',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    # URLs
    url='https://github.com/kullaniciadınız/gps-linker',
    project_urls={
        'Bug Reports': 'https://github.com/kullaniciadınız/gps-linker/issues',
        'Source': 'https://github.com/kullaniciadınız/gps-linker',
        'Documentation': 'https://github.com/kullaniciadınız/gps-linker#readme',
    },
    
    # Sınıflandırma
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Natural Language :: English',
        'Natural Language :: Turkish',
    ],
    
    # Anahtar kelimeler
    keywords=[
        'gps', 'exif', 'geotagging', 'photography',
        'maps', 'coordinates', 'metadata', 'exiftool',
        'google-maps', 'openstreetmap', 'gis'
    ],
    
    # Paketler
    py_modules=['gps_linker'],
    packages=find_packages(exclude=['tests', 'examples']),
    
    # Script'ler
    entry_points={
        'console_scripts': [
            'gps_linker=gps_linker:main',
            'gps-linker=gps_linker:main',
            'gpslinker=gps_linker:main',
        ],
    },
    
    # Bağımlılıklar
    python_requires='>=3.6',
    install_requires=[
        # Python standart kütüphanesi yeterli
    ],
    
    # Ekstra bağımlılıklar
    extras_require={
        'dev': [
            'black>=23.0.0',
            'flake8>=6.0.0',
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'mypy>=1.0.0',
        ],
        'test': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
        'docs': [
            'sphinx>=7.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
    },
    
    # Paket verileri
    package_data={
        '': ['README.md', 'LICENSE', 'requirements.txt'],
    },
    include_package_data=True,
    
    # Lisans
    license='MIT',
    
    # Platformlar
    platforms=['any'],
    
    # Sistem bağımlılıkları
    setup_requires=[
        # Kurulum sırasında gerekli paketler
    ],
    
    # Uzun açıklama
    long_description=long_description,
    
    # Download URL
    download_url='https://github.com/kullaniciadınız/gps-linker/releases',
)

if __name__ == '__main__':
    print(f"GPS Linker v{get_version()} kurulumu hazır!")
