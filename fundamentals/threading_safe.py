import concurrent.futures
import requests
import threading
import time

from requests.sessions import session

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.session()
    return thread_local.session

def download_site(url):
    # session = get_session()
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = ["https://www.jthon.org","http://olympus.realpython.org/dice",] *80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")