#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from urlparse import urlparse

import urllib2
def read_in_chunks(fobj, chunk_size=1024):
    while True:
        data = fobj.read(chunk_size)
        if not data:
            break
        yield

HEADERS = {
    'Accept':'*/*',
    'Accept-Charset':'UTF-8,*;q=0.5',
    'Accept-Encoding':'identity;q=1, *;q=0',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    #Host:m4.songtaste.com
    'Range':'bytes=0-',
    #Referer:http://m4.songtaste.com/201112212126/b4ffcbfa9c6f50416b61634bae1c63cc/4/4b/4b33cd91d48f88f474d9490bf3eb0715.mp3
    'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.121 Chrome/15.0.874.121 Safari/535.2',
}

def download(url, fname):
    HEADERS['Host'] = urlparse(url).netloc
    HEADERS['Referer'] = url
    req = urllib2.Request(url, headers=HEADERS)
    song = urllib2.urlopen(req)
    song_info = song.info()
    song_size = int(song_info.getheaders('Content-Length')[0])
    song_size_d = 0
    chunk_size = 1024*200
    with open(fname, 'wb') as f:
        #for piece in read_in_chunks(song, chunk_size):
            #print song_size_d/song_size, '% finished'
            #f.write(piece)
            #song_size_d += chunk_size
        while True:
            buf = song.read(chunk_size)
            if not buf: break
            f.write(buf)
            percent = (float(song_size_d)/float(song_size))*100
            print percent, '% finished'
            song_size_d += chunk_size

if __name__ == '__main__':
    download(sys.argv[1])
