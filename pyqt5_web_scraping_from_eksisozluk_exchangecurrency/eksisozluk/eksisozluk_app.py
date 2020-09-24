import sys
from PyQt5.QtWidgets import QWidget
import requests
from bs4 import BeautifulSoup as bs

def eksisozluk():
    url = 'https://eksisozluk.com/acemi-askere-yapilan-eziyet--6551657?a=popular'
    headers_param = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    r = requests.get(url,headers=headers_param)
    soup = bs(r.content,'html.parser')

    linkler = soup.find('ul', class_='topic-list partial').find_all('a', href=True,limit=50)

    data = {
            'Başlık': [],
            'Reyting': [],
            'Link': [],
            }
    for i in linkler:
        entry = i.get_text().split(' ')
        del entry[-1]
        entry = ' '.join(entry)
        data['Başlık'].append(entry)
        reyting = i.get_text().split(' ').pop()
        data['Reyting'].append(reyting)
        link = 'https://eksisozluk.com/' + i['href']
        data['Link'].append(link)
    return data