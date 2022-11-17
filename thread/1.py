import time
import concurrent.futures



img_urls = [
    'https://images.unsplash.com/photo-1517436073-7d3a1e2e9d0c?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3a6a6f2c2c3c4d5e6f7f8g9h0i1j2k3l&auto=format&fit=crop&w=1350&q=80',
    'https://images.unsplash.com/photo-1517436073-7d3a1e2e9d0c?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3a6a6f2c2c3c4d5e6f7f8g9h0i1j2k3l&auto=format&fit=crop&w=1350&q=80',
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

