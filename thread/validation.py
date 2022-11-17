import threading
import time
import sys
import multiprocessing
import concurrent.futures
import requests

img_urls = [
    'https://www.looper.com/img/gallery/this-huge-actor-is-reportedly-in-talks-to-return-as-spider-man/intro-1583531066.jpg',
    'https://images.prismic.io/mystique/5d7c09b9-40e5-4254-ae1c-2c1cb59aa898_IMG3.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
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
