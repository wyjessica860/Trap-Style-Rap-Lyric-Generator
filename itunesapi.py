import requests
import json
import requests
import webbrowser
# PYTHON GENIUS SCRAPER
from lxml import etree
import requests
from bs4 import BeautifulSoup
import os
import json
import time
import lyricsgenius
import sys
import codecs


with open('artists.json','r') as f:
    artists_dic = json.load(f)
artists = artists_dic['artists']

def itune_term(term):
    '''
    input: the term you want to search
    return a json of the search result
    '''
    term = term.replace(" ","+")
    url = f"https://itunes.apple.com/search?term={term}"
    response = requests.get(url)
    if response.status_code != 200:
        print("The URL is wrong!")
        return 404
    return json.loads(response.text)
songs_list = []

for artist in artists:
    resp_json = itune_term(artist)
    if resp_json == 404:
        continue
    
    for i in resp_json["results"]:
        try : 
            i["kind"]
        except:
            continue
        if i["kind"] == "song":
            songs_list.append(i['trackName'])

songs_dic = {"songs": songs_list}
with open('songs.json','w') as f:
    json.dump(songs_dic,f)

