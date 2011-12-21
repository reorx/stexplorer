#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import requests
import logging

logging.basicConfig(level=logging.INFO)


class HTTPFetchError(Exception):
    pass

class ST(object):
    prefix = 'http://'
    domain = 'www.songtaste.com'

    @classmethod
    def get_url(cls, rurl):
        return cls.prefix + cls.domain + rurl

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
        logging.info('get songurl success..')
        logging.info(songurl)
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

def get_songinfo(songid):
    songinfo = {
        'meta': {},
        'page_title': 'default',
        'mediatype': 'mp3',
    }
    resp = requests.get(ST.get_url('/song/%s/' % songid))
    if resp.status_code > 299:
        raise HTTPFetchError
    content = resp.content
    mediaargs_pattern = re.compile(r"""
    \<a\ href="javascript:playmedia1\(
        '\w+',
        '\w+',\s
        '(?P<strURL>\w+)',\s
        '\d+',\s
        '\d+',\s
        '(?P<md5_type>\w+)',\s
        '(?P<url_head>[\w:\/\.]+)',\s
        '(?P<songid>\d+)'
    """, re.X)
    mediaargs_search = mediaargs_pattern.search(content)
    if mediaargs_search is None:
        raise HTTPFetchError
    songinfo['meta'].update(mediaargs_search.groupdict())
    songinfo['mediatype'] = sim_GetSongType(songinfo['meta']['md5_type'])
    # TODO get more info from contents on page
    songdesc_pattern = re.compile(r"""
    \<p\ class="mid_tit"\>(?P<page_title>[^\<\>]+)\<\/p\>
    """, re.X)
    songdesc_search = songdesc_pattern.search(content)

    songinfo['page_title'] = songdesc_search.groups()[0]
    logging.info('get songinfo success..')
    return songinfo

def get_songurl(songinfo):
    meta = songinfo['meta']
    return sim_playmedia1(meta['strURL'], meta['md5_type'],
                          meta['url_head'], meta['songid'])

def clear_end_dot(name):
    while True:
        if not name.endswith('.'):
            return
        name = name[:-1]

def get_songfile(songurl, songinfo):
    # TODO write proper filename and id3 info by complete songinfo
    from downloader import download
    clear_end_dot(songinfo['page_title'])
    filename = songinfo['page_title'] + '.' + songinfo['mediatype']
    download(songurl, filename)
    logging.info('..done')

if '__main__' == __name__:
    songinfo = get_songinfo(sys.argv[1])

    songurl = get_songurl(songinfo)

    get_songfile(songurl, songinfo)
