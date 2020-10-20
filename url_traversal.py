from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_json(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup