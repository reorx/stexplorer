'''
Created on 2011-12-25

@author: reorx
'''
from distutils.core import setup
import py2exe #@UnusedImport

setup(
    name='ST Explorer',
    version='0.9.1',
    description='A SongTaste Downloading Tool',
    author='reorx',
    author_email='novoreorx@gmail.com',
    packages=['stex'],
    package_dir={'stex': 'stex'},
    # below is arguments used by py2exe
    options={
        'py2exe': {
            'includes': ['sip'],
        }
    },
    windows=['stex/maingui.py'],
)