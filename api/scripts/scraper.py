from bs4 import BeautifulSoup
import requests


def parse_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for a in soup.find_all('a'):
        if a.find('h1'):
            print(a.find('h1').text)

def run():
    urls = [
        'https://www.remoteimpact.io/'
    ]

    for url in urls:
        parse_page(url)