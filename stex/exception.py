'''
Created on 2011-12-25

@author: reorx
'''

import logging

class BaseError(Exception):
    def __init__(self, msg):
        self.msg = msg
        logging.error(self.__class__.__name__ + ': ' + msg)    

class HTTPFetchError(BaseError):
    pass