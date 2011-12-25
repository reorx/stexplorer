'''
Created on 2011-12-25

@author: reorx
'''
import re
import os
import requests
import logging

from stex import settings
from stex.exception import BaseError, HTTPFetchError

class ST(object):
    URL_PREFIX = 'http://'
    DOMAIN = 'www.songtaste.com'

    @classmethod
    def get_url(cls, rurl):
        return cls.URL_PREFIX + cls.DOMAIN + rurl

def sim_playmedia1(
        strURL,
        md5_type,
        url_head,
        songid):
    songurl = None
    if 'rayfile' in strURL:
        songurl = url_head + strURL + sim_GetSongType(md5_type)
    else:
        post_data = {
            'str': strURL,
            'sid': songid,
        }
        resp = requests.post(ST.get_url('/time.php'), post_data)
        if resp.status_code > 299:
            raise HTTPFetchError
        songurl = resp.content
        logging.debug('sim_playmedia1: get songurl')
        logging.debug(songurl)
        return songurl

def sim_GetSongType(md5):
    typeDict = {
        "7d99bb4c7bd4602c342e2bb826ee8777": "wma",
        "25e4f07f5123910814d9b8f3958385ba": "Wma",
        "51bbd020689d1ce1c845a484995c0cce": "WMA",
        "b3a7a4e64bcd8aabe4cabe0e55b57af5": "mp3",
        "d82029f73bcaf052be8930f6f4247184": "MP3",
        "5fd91d90d9618feca4740ac1f2e7948f": "Mp3",
    }
    return typeDict[md5]

class STPageParser(object):
    """
    songinfo::
        :id3
            :title
            :artist
            :album
            :organization
            :website
        :ST
            :recommender
                :username
                :id - str
            :songid - str
        :meta
            :strURL
            :md5_type
            :url_head
            :songid
        :_url
        :_mediaurl
        :_mediatype
    """
    
    class ParseError(BaseError):
        pass
    
    def __init__(self, songid):
        self.songinfo = {}
        self.songinfo['ST'] = {
            'songid': songid,
        }
        self.songinfo['_url'] = ST.get_url('/song/%s/' % songid)
        self.songinfo['id3'] = {
            'album': getattr(settings, 'ID3_ALBUM', 'SongTaste'),
            'organization': getattr(settings, 'ID3_ORGANIZATION', 'ST Explorer'),
            'website': self.songinfo['_url'],
        }
        
    def _search(self, ptn_str, info_key=None):
        ptn = re.compile(ptn_str, re.X)
        searched = ptn.search(self.content)
        if not searched:
            raise STPageParser.ParseError(info_key or 'unexpected unknown info key')
        return searched
        
    def _search_one(self, ptn_str, **kwgs):
        searched = self._search(ptn_str, **kwgs)
        return searched.groups()[0]
    
    def _search_many(self, ptn_str, **kwgs):
        searched = self._search(ptn_str, **kwgs)
        return searched.groupdict()
    
    def info_meta(self):
        logging.debug('parse meta')
        ptn_str = r"""
        \<a\ href="javascript:playmedia1\(
            '\w+',
            '\w+',\s
            '(?P<strURL>\w+)',\s
            '\d+',\s
            '\d+',\s
            '(?P<md5_type>\w+)',\s
            '(?P<url_head>[\w:\/\.]+)',\s
            '(?P<songid>\d+)'
        """

        meta = self._search_many(ptn_str)
        
        self.songinfo['_mediaurl'] = sim_playmedia1(
                meta['strURL'], meta['md5_type'],
                meta['url_head'], meta['songid'])
        self.songinfo['_mediatype'] = sim_GetSongType(meta['md5_type'])
        self.songinfo['meta'] = meta
    
    def info_id3(self):
        logging.debug('parse id3')
        ptn_str = r"""
        \<p\ class="mid_tit"\>(?P<title>[^\<\>]+)\<\/p\>
        """
        self.songinfo['id3']['title'] = self._search_one(ptn_str)
        clean_end(self.songinfo['id3']['title'])
        
        ptn_str = r"""
        \<h1\ class="h1singer"\>(?P<artist>.*)\<\/h1\>
        """
        self.songinfo['id3']['artist'] = self._search_one(ptn_str)
    
    def info_ST(self):
        logging.debug('parse ST')
        ptn_str = r"""
        \<p\ class="fir_rec"\>
        \s+.+\s+.+\s+.+\s+.+\s+
        \<a\ href="(?P<rurl>.+)"\ class="underline"\>
        (?P<username>.+)\<\/a\>
        """
        st = self._search_many(ptn_str, info_key='ST')
        logging.info(str(st))
        self.songinfo['ST']['recommender'] = {
            'username': st['username'],
            'id': st['rurl'].split('/')[1],
        }
    
    def parse(self):
        logging.debug('parse')
        resp = requests.get(self.songinfo['_url'])
        if resp.status_code > 299:
            raise HTTPFetchError('get page failed') # TODO resp error message
        self.content = resp.content
        print type(self.content)
        self.content = self.content.decode('gbk')
        
        self.info_meta()
        self.info_id3()
        self.info_ST()
        
        logging.info('\n' + str(self.songinfo))
        return self.songinfo


def clean_end(name):
    """
    clean dot and other strange chars which may infulence id3 data set
    """
    while True:
        if not name.endswith('.') and not name.endswith(' '):
            return
        name = name[:-1]
        
def get_songid_from_alternative(s):
    from urlparse import urlparse
    if s.startswith('http://'):
        if s.endswith('/'):
            s = s[:-1]
        oUrl = urlparse(s)
        return oUrl.path.split('/')[-1]
    else:
        return s
        
def get_songinfo(songid):
    songinfo = STPageParser(songid).parse()
    return songinfo

def make_fpath(songinfo):
    song_title = songinfo['id3']['title']
    fname = song_title + '.' + songinfo['_mediatype']
    dir_str = getattr(settings, 'DOWNLOAD_PATH', 'download')
    # check if exists
    if os.path.isabs(dir_str):
        dirpath = dir_str
    else:
        root = os.path.join(os.getcwd(), '../')
        dirpath = os.path.join(root, dir_str)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
    fpath = os.path.abspath(os.path.join(dirpath, fname))
    return fpath

