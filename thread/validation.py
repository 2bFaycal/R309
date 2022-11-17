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


def task_threading():
    t1 = threading.Thread(target=download_image, args=(img_urls[0],))
    t2 = threading.Thread(target=download_image, args=(img_urls[1],))
    t3 = threading.Thread(target=download_image, args=(img_urls[2],))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
def task_multiprocessing ():
    p1 = multiprocessing.Process(target=download_image, args=(img_urls[0],))
    p2 = multiprocessing.Process(target=download_image, args=(img_urls[1],))
    p3 = multiprocessing.Process(target=download_image, args=(img_urls[2],))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()


def task_pool():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_image, img_urls)


if __name__ == '__main__':
    start = time.perf_counter()
    task_threading()
    finish = time.perf_counter()
    print(f'THREADING in {round(finish-start, 3)} second(s)')

    start = time.perf_counter()
    task_multiprocessing()
    finish = time.perf_counter()
    print (f"MULTIPROCCESING dans {round(finish-start, 3)} second(s)")

    start = time.perf_counter()
    task_pool()
    finish = time.perf_counter()
    print(f'POOL in {round(finish-start, 3)} second(s)')


