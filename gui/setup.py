#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This setup file is just used for py2exe packaging

from distutils.core import setup
import py2exe

setup(
    name='STExplorer',
    version='0.9.1',
    description='A SongTaste Downloading Tool',
    author='reorx',
    author_email='novoreorx@gmail.com',
    # below is arguments used by py2exe
    options={
        'py2exe': {
            'includes': ['sip'],
        }
    },
    windows=['stexplorer.py'],
)
