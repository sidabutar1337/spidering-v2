#/bin/python
#coded by zeussec1337
import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
def running_text(text):
    for teks in text + '\n': 
        sys.stdout.write(teks)
        sys.stdout.flush()
        time.sleep(0.05)
ascii_art = r'''
         (
               )
              (
        /\  .-"""-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"""-;///\\
      //  \/   .   \/  \\ WEB SPIDER V 2.1
     (| ,-_| \ | / |_-, |)DEVELOPER:SIDABUTARXCODE (ZEUSSEC1337)
       //`__\.-.-./__`\\  GITHUB:SIDABUTAR1337
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/
'''
NOTE = '''
halo script kiddies!!
script ini di buat untuk pembelajaran
ini membantu anda menemukan lokasi halaman
pada subdomain yang sudah anda kumpulkan
alat ini akan membantu anda menemukan halaman
parameter hingga halaman login'''
running_text(ascii_art)
running_text(NOTE)
file = input("File: ")
if os.path.exists(file):
    with open(file,'r') as files:
        read_data = files.readlines()
        for url in read_data:
            urls = url.strip()
            try:
                response = requests.get(urls)
                time.sleep(0.05)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text,'html.parser')
                    page = soup.find_all('a')
                    for pages in page:
                        if 'href' not in pages.attrs:
                            continue
                        if 'http' not in pages['href'] and 'https' not in pages['href']:
                            found_page = pages['href']
                            joinurl = urljoin(urls,str(found_page))
                            print(f'Pages:{joinurl}')
                        else:
                            redirect = pages['href']
                            print(f'Redirect:{redirect}')
                    images = soup.find_all('img')
                    for img in images:
                        if 'src' not in img.attrs:
                            gambar = img['src']
                            print(f'Images:{gambar}')
                            continue
                else:
                    print(f'{urls} tidak bisa di jangkau')
            except requests.exceptions.ConnectionError as E:
                print('koneksi bermasalah: ',E)
            except requests.exceptions.Timeout:
                print('Waktu Koneksi habis')
            except requests.exceptions.HTTPError:
                print('HTTP bermasalah')
            except requests.exceptions.RequestException as e:
                print('Terjadi kesalahan lain: ',e)
else:
    print('File tidak ada')    
