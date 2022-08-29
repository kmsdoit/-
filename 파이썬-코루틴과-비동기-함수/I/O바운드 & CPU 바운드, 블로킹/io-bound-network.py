import re
import requests

def io_bound_func():
    result = requests.get('http://203.243.17.90:80')
    
    return result

if __name__ == '__main__':
    for i in range(10):
        result = io_bound_func()
        
    print(result)