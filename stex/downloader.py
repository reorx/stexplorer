# -*- coding: utf-8 -*-
'''
Created on 2011-12-23

@author: reorx
'''

import os
import urllib2
from urlparse import urlparse


HEADERS = {
    'Accept': '*/*',
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Range': 'bytes=0-',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.121 Chrome/15.0.874.121 Safari/535.2',
}


def read_in_chunks(fobj, chunk_size=1024):
    while True:
        data = fobj.read(chunk_size)
        if not data:
            break
        yield


def fetch_file_resp(url):
    HEADERS['Host'] = urlparse(url).netloc
    HEADERS['Referer'] = url
    req = urllib2.Request(url, headers=HEADERS)
    resp = urllib2.urlopen(req)
    return resp


def mkdir(dirpath):
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)


def download(url, fname, dirpath=None, chunk_size=1024 * 500):
    print '## url', url
    HEADERS['Host'] = urlparse(url).netloc
    HEADERS['Referer'] = url
    print '## headers', HEADERS
    #req = urllib2.Request(url, headers=HEADERS)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    resp_info = resp.info()
    song_size = int(resp_info.getheaders('Content-Length')[0])
    song_size_d = 0

    if dirpath is None:
        fpath = fname
    else:
        fpath = os.path.join(dirpath, fname)
    with open(fpath, 'wb') as f:
        #for piece in read_in_chunks(resp, chunk_size):
            #print song_size_d/song_size, '% finished'
            #f.write(piece)
            #song_size_d += chunk_size
        while True:
            buf = resp.read(chunk_size)
            if not buf:
                break
            f.write(buf)
            percent = (float(song_size_d) / float(song_size)) * 100
            print percent, '% finished'
            song_size_d += chunk_size
    return os.path.abspath(fpath)
