'''
Created on 2011-12-25

@author: reorx
'''
from setuptools import setup
import py2exe

setup(
    name='ST Explorer',
    version='0.9.1',
    description='A SongTaste Downloading Tool',
    author='reorx',
    author_email='novoreorx@gmail.com',
    packages=['stex'],
    package_dir={'stex': 'stex'},
    install_requires=[
        'requests'
    ],

    # py2exe options
    options={
        'py2exe': {
            'includes': ['sip'],
        }
    },
    windows=['stex/maingui.py'],
)
