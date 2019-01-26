import aiohttp
import asyncio
import os
import re
import threading
import time
import urllib.request

URL = 'https://www.python.org/downloads/source/'


def get_links_for_download():
    response = urllib.request.urlopen(URL)
    return re.findall(r'Download <a href="(.*?)">', str(response.read()))


def download_bunch_of_files(link):
    urllib.request.urlretrieve(link)


def start_thr(links):
    _list_of_thr = []
    start_time = time.time()

    for link in links:
        t = threading.Thread(target=download_bunch_of_files, args=(link,))
        t.start()
        _list_of_thr.append(t)
    for i in _list_of_thr:
        i.join()

    print("Download all bunches with threads from {},"
          "took {:.2f} sec".format(URL, time.time() - start_time))


@asyncio.coroutine
async def download_coroutine(url):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as f_handle:
                while True:
                    chunk = await response.content.read(8192)
                    if not chunk:
                        break
                    f_handle.write(chunk)

            return await response.release()


async def download_multiple(links):
    start_time = time.time()

    tasks = [asyncio.create_task(download_coroutine(link)) for link in links]
    await asyncio.gather(*tasks)

    print("Download all bunches with asyncio from {},"
          " took {} sec".format(URL, time.time() - start_time))

links = get_links_for_download()

print('Threads:')
start_thr(links)

print('Asynchronous:')
loop = asyncio.get_event_loop()
result = loop.run_until_complete(download_multiple(links))
loop.close()
