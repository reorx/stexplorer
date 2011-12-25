#!/usr/bin/python
'''
Created on 2011-12-25

@author: reorx
'''
import os
import sys

import settings
from parse import STPageParser, get_songid_from_alternative #@UnresolvedImport
from downloader import download #@UnresolvedImport

def easy_work(songid):
    songinfo = STPageParser(songid).parse()
    song_title = songinfo['id3']['title']
    fname = song_title + '.' + songinfo['_mediatype']
    dir_str = getattr(settings, 'DOWNLOAD_PATH', 'download')
    # check if exists
    if os.path.isabs(dir_str):
        dirpath = dir_str
    else:
        root = os.path.join(os.path.dirname(__file__), '../')
        dirpath = os.path.join(root, dir_str)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
    fpath = download(songinfo['_mediaurl'],
                     fname, dirpath)
    print fpath
    from song import reset_id3
    reset_id3(fpath, songinfo)
    

    

if '__main__' == __name__:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    strInput = sys.argv[1]
    songid = get_songid_from_alternative(strInput)
    easy_work(songid)