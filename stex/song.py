# -*- coding: utf-8 -*-
'''
Created on 2011-12-23

@author: reorx
'''
from mutagen.easyid3 import EasyID3

def reset_id3(fpath, songinfo):
    """
    songinfo::
        :title
        :artist
        :recommender
        :website
    """
    sid3 = EasyID3(fpath)
    for i in sid3.iterkeys():
        sid3[i] = None
    for i in ('title', 'artist', 'recommender', 'website'):
        sid3[i] = songinfo[i]
    sid3.save()