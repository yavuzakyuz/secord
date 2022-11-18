import requests
from bs4 import BeautifulSoup
 

def get_api(url):
    try:    
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
    except:
        return ("error")


