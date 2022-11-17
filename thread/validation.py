import threading
import time
import sys
import multiprocessing
import concurrent.futures
import requests


img_urls = [
    'https://i.pinimg.com/474x/d9/48/d9/d948d9aec4b82b0df940b953da2fc0f5.jpg',
    'https://i.pinimg.com/474x/13/37/ed/1337ed4377c6b79e997046823bf57533.jpg',
    'https://i.pinimg.com/474x/fb/08/94/fb0894bd74afe91b0c787684679c01dd.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[5]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded..')


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

finish = time.perf_counter()
print (f'Finished in {round(finish-start, 2)} second(s)')

def task ():
    print (f"start for 1 sec")
    time.sleep(1)
    print (f"FINITO")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print (f"FINITO dans {round(end-start, 2)} second(s)")


