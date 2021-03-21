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

"""
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
"""
genius = lyricsgenius.Genius("gulqB5H9cGgsk2Hzo5jX96Q2QAQrMJp2eSF66WUAShkpJxQG8kh0rd1UrJBY8HK5")
with open('artists.json','r') as f:
    artists_dic = json.load(f)
artists = artists_dic['artists']
with open('data/singer.txt','r') as f:
    sing_already = f.read()
artists = artists_dic['artists']

for a in artists:
    if a in sing_already:
        continue
    try:
        artist = genius.search_artist(a, max_songs=30, sort='popularity',include_features=True)
    except:
        time.sleep(10)
        try: 
            artist = genius.search_artist(a, max_songs=20, sort='popularity',include_features=True)
        except:
            time.sleep(10)
            try: 
                artist = genius.search_artist(a, max_songs=10, sort='popularity',include_features=True)
            except:
                time.sleep(10)
                try: 
                    artist = genius.search_artist(a, max_songs=4, sort='popularity',include_features=True)
                except:
                    continue

    try:
        sum = 0
        for i in artist.songs:
            lyrics = artist.song(i.to_dict()['title']).lyrics
            with open('data/input_lyrics.txt', 'a',encoding='utf8') as f:
                f.write("##########################################")
                f.write(a)
                f.write(i.to_dict()['title'])
                f.write(lyrics)
                f.close()
            sum +=1
    except:
        continue
    with open('data/singer.txt', 'a',encoding='utf8') as f:
        f.write(a)
        f.write(", ")
        f.write(str(sum)+'\n')
        f.close()


        
