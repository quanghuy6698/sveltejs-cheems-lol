import json


with open('champions.json', encoding="utf8") as rfile:
  data = json.load(rfile)
  data2 = []
  for champ in data:
    champImg = champ['id'] + '.jpg'
    champ2 = {
      "id": champ['id'],
      "key": champ['key'],
      "name": champ['name'],
      "title": champ['title'],
      "tags": champ['tags'],
      "stats": champ['stats'],
      "description": champ['description'],
      "img": champImg
    }
    data2.append(champ2)

  with open('new.json', 'w') as outfile:
    json.dump(data2, outfile)

