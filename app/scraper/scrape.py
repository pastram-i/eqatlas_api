from app.scraper.zone_details import parse_zone

import json

def run():
    with open ('app/data/zones.json', 'r') as openfile:
        j = json.load(openfile)

    for idx, z in enumerate(j):
        try:
            #j[idx] = {z['URL Name'] : parse_zone(z)}
            j[idx] = {k : parse_zone(v) for k,v in j[idx].items()}
        except Exception:
            print(f'\n***\nFailed to parse {z}\n***\n')

#TODO: Parse image?
#https://wiki.project1999.com/Zone_Connection_World
#Ports, connection types, etc.

    with open('app/data/zones.json', 'w') as outfile:
        json.dump(j, outfile)