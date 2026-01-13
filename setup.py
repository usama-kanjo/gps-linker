#!/usr/bin/env python3
"""
GPS Linker - Kurulum dosyası
"""

from setuptools import setup
import re

def get_version():
    """gps_linker.py dosyasından versiyonu al"""
    try:
        with open('gps_linker.py', 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", content)
            if match:
                return match.group(1)
    except FileNotFoundError:
        pass
    return '1.0.0'

def get_long_description():
    """README.md'den açıklamayı al"""
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Fotoğraflardan GPS bilgilerini çıkarır ve harita linkleri oluşturur"

setup(
    name='gps-linker',
    version=get_version(),
    
    author='Usama Kanjo',
    author_email='email@adresiniz.com',
    description='Fotoğraflardan GPS bilgilerini çıkarır ve harita linkleri oluşturur',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    
    url='https://github.com/usama-kanjo/gps-linker',
    project_urls={
        'Bug Reports': 'https://github.com/usama-kanjo/gps-linker/issues',
        'Source': 'https://github.com/usama-kanjo/gps-linker',
        'Documentation': 'https://github.com/usama-kanjo/gps-linker#readme',
    },
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Natural Language :: Turkish',
    ],
    
    keywords=['gps', 'exif', 'geotagging', 'photography', 'maps', 'coordinates'],
    
    py_modules=['gps_linker'],
    
    entry_points={
        'console_scripts': [
            'gps_linker=gps_linker:main',
        ],
    },
    
    python_requires='>=3.6',
    
    license='MIT',
)
