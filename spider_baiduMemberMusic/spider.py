#-*-coding: utf-8-*-
#_author_: Mr. liu 2/16/2018
import requests
import re
import json
url='http://zhangmenshiting.qianqian.com/data2/music/e93d963095b109ff47de85f1b41ffdd1/522883870/522883870.mp3?xcode=6e9488a8cbd8a0a4ec0a60cf41a4a187'
#respond=requests.get(url)
#http://ting.baidu.com/data/music/links?songIds=<songIds>
#print (respond.content)
#with open('text.mp3', 'wb') as f:
#    f.write(respond.content)
def get_song_by_id(id):
    song_id=id
    api ='http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17205500581185420972_1513324047403&songid=%s&_=1513324048127' % song_id
    response=requests.get(api)
    data=response.text
    data=re.findall(r'\((.*)\)',data)[0]
    data = json.loads(data)
    title=data['songinfo']['title']
    DLink=data['bitrate']['show_link']
    print (title)
    print (DLink)
    #Downloading


    data=requests.get(DLink).content
    with open('%s.mp3' % title, 'wb') as f:
        f.write(data)
def get_songid_by_singer(name):
    
    url='http://music.baidu.com/search'
    data = {
        'key':name
    }
    response=requests.get(url,params=data)
    response.encoding='utf-8'

    html=response.text
    ul=re.findall(r'<ul.*</ul>',html,re.S)[0]
    #may change to .*????
    sids=re.findall(r'sid&quot;:(.*?),',ul,re.S)
    print (sids)
    return sids

sids=get_songid_by_singer('duff')
print (sids)
for sid in sids:
    get_song_by_id(sid)