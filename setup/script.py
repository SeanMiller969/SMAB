import requests
import json
from bs4 import BeautifulSoup

URL = "https://steamcommunity.com/market/listings/730/Operation Riptide Case"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all(type="text/javascript")

start = results[-1].text.find("var g_rgAssets")
end = results[-1].text.find(";", start)
print(results[-1].text[start + 17:end])
test = json.loads(results[-1].text[start + 17:end])
key = list(test['730']['2'].keys())[0]
print(test['730']['2'][key]['descriptions'])