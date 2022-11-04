import requests
import re
from bs4 import BeautifulSoup
import json

# Program pokazuje aktualne wątki z forum gry przeglądarkowej mojego dzieciństwa i zwraca je do jsona

req = requests.get('https://forum.the-west.pl/index.php?whats-new/posts/922739/')
soup = BeautifulSoup(req.text, 'html.parser')
actual_forum = []
for date in soup.findAll('div', {'class': 'structItem-title'}):
    span = str(date.find('a'))
    found = re.search('>(.+?)</a>', span).group(1)
    print(found)
    actual_forum.append(found)
for el in actual_forum:
    el.encode('utf-8')
with open('actual_forum.json', 'w', encoding='utf-8') as f:
    json.dump(actual_forum, f, ensure_ascii=False)
