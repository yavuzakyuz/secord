import requests
from bs4 import BeautifulSoup
 

def get_code(url):
    try:    
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
    except:
        return ("error")
  
    f = open("fetched_html.txt", "w")
    f.write(str(soup))
    f.close()
    return ("success")


# for link in soup.find_all('a'):
#     print(link.get('href'))