# -*- coding: utf-8 -*-

import numpy as np
import asyncio
import json

import logging
import uuid
from typing import Union, Sequence


from storage import HeapPersistentStorage

class clientlat:
    def __init__(self,protocol,msg_size):
        self.protocol=protocol
        self.ln=msg_size;
        self.xxpow =1
        self.xxmul =1
        self.xxdiv =1
        self.xmul =1
        self.xdiv =1
        self.xadd =0 
        self.add =0
        self.xxadd=0
    def latency(self):
        if self.protocol == 'mqttsn':
            self.xxmul=0
            self.xdiv = self.ln**0.5
            self.add=19
        elif self.protocol == 'coap':
            self.xxdiv=46
            self.xxpow=0.9
            self.xmul = 0
            self.add=19
        elif self.protocol == 'http':
            self.xxdiv=79
            self.xxpow=1.2
            self.xmul = 0
            self.add= 19
        elif self.protocol == 'smqtt':
            self.xxdiv=74598765
            self.xxpow=2
            self.xdiv = 69
            self.add=17
        elif self.protocol == 'dds':
            self.xxmul=0
            self.xdiv = 468
            self.xmul=11
            self.add=211
        lat= self.xxmul*(self.ln**self.xxpow+self.xxadd)/self.xxdiv +self.xmul*(self.ln+self.xadd)/self.xdiv+self.add

        return lat;
 
        
    