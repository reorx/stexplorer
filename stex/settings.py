# -*- coding: utf-8 -*-
'''
Created on 2011-12-23

@author: reorx
'''
ID3_ALBUM = 'SongTaste.Col'
ID3_ORGANIZATION = 'Reorx Workshop'

# relative root is stexplorer/ folder
# absolute path is also fines
DOWNLOAD_PATH = 'download'

if '__main__' == __name__:
    print __file__
    import os
    print os.path.dirname(__file__)