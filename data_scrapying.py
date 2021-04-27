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
import pandas as pd
'''
artists_list = []
for i in range(1,23):
    response_artists = requests.get(f"https://www.last.fm/tag/trap+rap/artists?page={i}")
    re_tree = etree.HTML(response_artists.text)
    artists_list = artists_list + re_tree.xpath('//*[@class="big-artist-list-title"]/a/text()')
artists_dic = {}
artists_dic['artists'] = artists_list

with open('artists.json','w') as f:
    json.dump(artists_dic,f)

'''
lyrics_df = pd.DataFrame({'singer':[],'title':[],'lyrics':[]})
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
            lyrics_df = pd.concat([lyrics_df,pd.DataFrame({'singer':[a],'title':[i.to_dict()['title']],'lyrics':[lyrics]})])

            sum +=1
    except:
        continue
    with open('data/singer.txt', 'a',encoding='utf8') as f:
        f.write(a)
        f.write(", ")
        f.write(str(sum)+'\n')
        f.close()
    lyrics_df.to_csv('wn21630project_lyrics_input.csv')


        
