'''
Created on 2011-12-25

@author: reorx
'''
from setuptools import setup

setup(
    name='stex',
    version='0.9.1',
    description='Core module of ST Explorer',
    author='reorx',
    author_email='novoreorx@gmail.com',
    packages=['stex'],
    install_requires=[
        'requests'
    ],
)
