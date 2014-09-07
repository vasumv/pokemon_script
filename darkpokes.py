from bs4 import BeautifulSoup
import requests
url = "http://pokemondb.net/type/dark"
r = requests.get(url)
data = r.text
pokes = []
f = open("darkpokes.txt", 'a')
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    text = link.get("href")
    if "pokedex" in text:
        pokemon = text[9:]
        pokes.append(pokemon)
f.write('\n'.join(pokes))

