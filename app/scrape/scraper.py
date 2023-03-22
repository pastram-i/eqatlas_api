from scrape.zone_details import zone

import json

def run():
    with open ('app/src/zones.json', 'r') as openfile:
        j = json.load(openfile)

    for idx, z in enumerate(j):
        #TODO: Fix unique cases
        #https://wiki.project1999.com/Stonebrunt_Mountains
        #https://wiki.project1999.com/The_Warrens
        #https://wiki.project1999.com/Kaladim
        #https://wiki.project1999.com/Chardok
        j[idx] = zone(j[idx])

#TODO: Parse image?
#https://wiki.project1999.com/Zone_Connection_World
#Ports, connection types, etc.

    with open('app/src/zones.json', 'w') as outfile:
        json.dump(j, outfile)