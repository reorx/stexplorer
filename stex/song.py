# -*- coding: utf-8 -*-
'''
Created on 2011-12-23

@author: reorx
'''
from mutagen.easyid3 import EasyID3

def force_unicode(s):
    if not isinstance(s, unicode):
        s = s.decode('utf8')
    return s

def reset_id3(fpath, songinfo):
    """
    songinfo::
        :title
        :artist
        :recommender
        :website
    
    NOTE values in songinfo must be unicode, or utf8 str
    """
    sid3 = EasyID3(fpath)
    # TODO sid3 reset problems...
#    for i in sid3.iterkeys():
#        sid3[i] = u''
    for i in songinfo['id3']:    
        value = force_unicode(songinfo['id3'][i])
        print i, ':', value
        sid3[i] = value
    sid3.save()


if __name__ == '__main__':
    sid3 = EasyID3('D:\Paradise\EWorkspace\stexplorer\download\The Last Castrato.mp3')
    print dir(sid3)
    sid3['title'] = 'hello'
    sid3['artist'] = u'音乐品尝'
    sid3.save()