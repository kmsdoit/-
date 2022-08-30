import requests

# 세션: 서버와 클라이언트를 지속적으로 이어주는 것

def fetcher(session,url):
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://naver.com","https://google.com","https://instagram.com"]

    with requests.Session() as session:
        result = [fetcher(session,url) for url in urls]
        print(result)
    

if __name__ == '__main__':
    main()