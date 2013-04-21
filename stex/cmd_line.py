#!/usr/bin/python
'''
Created on 2011-12-25

@author: reorx
'''
import os
import sys

from stex import settings
from stex.parse import STPageParser, get_songid_from_alternative
from stex.downloader import download

def easy_work(songid):
    songinfo = STPageParser(songid).parse()
    song_title = songinfo['id3']['title']
    fname = song_title + '.' + songinfo['_mediatype']
    dir_str = 'download'
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
    from stex.song import reset_id3
    reset_id3(fpath, songinfo)




if '__main__' == __name__:
    import logging
    logging.basicConfig(level=logging.DEBUG)

    strInput = sys.argv[1]
    songid = get_songid_from_alternative(strInput)
    easy_work(songid)
