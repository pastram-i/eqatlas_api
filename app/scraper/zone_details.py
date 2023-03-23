import requests
from bs4 import BeautifulSoup

def formatter(zone):
    try:
        #Some data housekeeping, don't use 'null'
        zone['Name in /who'] = zone['Name in /who'] or "n/a"
        zone['Full URL'] = zone['Full URL'] or "n/a"
        zone['ZEM Value'] = zone['ZEM Value'] or "n/a"
        zone['Zone Spawn Timer'] = zone['Zone Spawn Timer'] or "n/a"
        zone['Inactive'] = bool(zone['Inactive'])
        zone['46+'] = bool(zone['46+'])
        zone['Key Required'] = bool(zone['Key Required'])
        zone['Shaman Port'] = bool(zone['Shaman Port'])
        zone['Druid Port'] = bool(zone['Druid Port'])
        zone['Wizard Port'] = bool(zone['Wizard Port'])
        zone['Firepot Port'] = bool(zone['Firepot Port'])
        zone['Adjacent Zones'] = zone['Adjacent Zones'] or []
        zone['Ocean Connections'] = zone['Ocean Connections'] or []
        zone['1 Way Connections'] = zone['1 Way Connections'] or []
        zone['Level of Monsters'] = zone['Level of Monsters'] or []
        zone['Types of Monsters'] = zone['Types of Monsters'] or []
        zone['Notable NPCs'] = zone['Notable NPCs'] or []
        zone['Unique Items'] = zone['Unique Items'] or []
        zone['Succor/Evacuate'] = zone['Succor/Evacuate'] or []
        zone['Related Quests'] = zone['Related Quests'] or []
        zone['Guilds'] = zone['Guilds'] or []
        zone['City Races'] = zone['City Races'] or []
        zone['Tradeskill Facilities'] = zone['Tradeskill Facilities'] or []
        zone['Player Guides'] = zone['Player Guides'] or []
    except:
        print(f'\n***\nFailed to format {zone["Full URL"]}\n***')
        print(zone+"\n")
    return zone

def parse_zone(zone):
    url = zone['Full URL']
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(class_="zoneTopTable")
    special_pages = ['https://wiki.project1999.com/Stonebrunt_Mountains', 'https://wiki.project1999.com/The_Warrens', 'https://wiki.project1999.com/Kaladim', 'https://wiki.project1999.com/Chardok']
    if url not in special_pages:
        for row in table.find_all('tr'):
            h = row.find('b').text.strip().replace(':', '')
            if h in zone.keys():
                val = []
                if h in ['Adjacent Zones','Notable NPCs','Related Quests','Guilds','City Races','Tradeskill Facilities','Player Guides']:
                    vals = row.find_all('a')
                    val.extend(
                        {
                            'name': v.text.strip(),
                            'link': 'https://wiki.project1999.com' + v['href'],
                        }
                        for v in vals
                    )
                elif h in ['Unique Items']:
                    items = row.find_all(class_='hbdiv')
                    val.extend(
                        {
                            'name': i.find('a').text.strip(),
                            'link': 'https://wiki.project1999.com'
                            + i.find('a')['href'],
                            'details': i.find('p').text.strip().split('\n'),
                        }
                        for i in items
                    )
                elif h in ['Level of Monsters','Succor/Evacuate', 'Zone Spawn Timer']:
                    #TODO: format better
                    pass
                else:
                    val = row.find('td').text.strip().split(',')
                zone[h] = val
    return formatter(zone)