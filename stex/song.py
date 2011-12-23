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
    # TODO sid3 reset problems...
#    for i in sid3.iterkeys():
#        sid3[i] = ''
    for i in songinfo['id3']:
        print i, ':', songinfo['id3'][i]
        sid3[i] = unicode(songinfo['id3'][i], 'utf8')
    sid3.save()


if __name__ == '__main__':
    sid3 = EasyID3('D:\Paradise\EWorkspace\stexplorer\download\The Last Castrato.mp3')
    print dir(sid3)
    sid3['title'] = 'hello'
    sid3['artist'] = '音乐品尝'
    sid3.save()