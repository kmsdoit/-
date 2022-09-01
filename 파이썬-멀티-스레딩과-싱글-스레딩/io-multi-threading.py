
from concurrent.futures import ThreadPoolExecutor
import os
import re
import threading
import requests
import time

def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid} process | {threading.get_ident()} url: {url}")
    with session.get(url) as response:
        return response.text
    
def main():
    urls = ["https://apple.com","https://google.com","https://github.com"] * 50
    
    executor = ThreadPoolExecutor(max_workers=10) # 멀티 쓰레딩 
     
    with requests.Session() as session:
        # result = [fetcher(session,url) for url in urls]
        # print(result)
        params = [(session,url) for url in urls]
        results = list(executor.map(fetcher,params))
        print(results)
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"process time: {end-start}")