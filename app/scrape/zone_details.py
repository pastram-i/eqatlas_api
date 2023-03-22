import requests
from bs4 import BeautifulSoup

def zone(zone):
    url = zone['Full URL']
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(class_="zoneTopTable")
    try:
        for row in table.find_all('tr'):
            h = row.find('b').text.strip().replace(':', '')
            if h in zone.keys():
                val = []
                if h in ['Notable NPCs','Unique Items', 'Related Quests', 'Adjacent Zones', 'City Races', 'Guilds', 'Tradeskill Facilities', 'Player Guides']:
                    vals = row.find_all('a')
                    for v in vals:
                        val.append({'name': v.text.strip(), 'link': 'https://wiki.project1999.com'+v['href']})
                #TODO: Add item details
                else:
                    val = row.find('td').text.strip().split(',')
                zone[h] = val[0] if len(val) == 1 else val
        return zone
    except:
        print(url)