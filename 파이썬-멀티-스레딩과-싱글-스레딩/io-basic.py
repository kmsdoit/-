import asyncio
import requests
import aiohttp

# 세션: 서버와 클라이언트를 지속적으로 이어주는 것

async def fetcher(session,url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://naver.com","https://google.com","https://instagram.com"]

    async with aiohttp.ClientSession() as session:
        # result = [fetcher(session,url) for url in urls]
        # print(result)
        result = await asyncio.gather(*[fetcher(session,url) for url in urls]) # unpacking
        print(result) 
    

if __name__ == '__main__':
    asyncio.run(main())
    
    