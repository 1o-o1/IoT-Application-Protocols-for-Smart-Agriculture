# -*- coding: utf-8 -*-

import numpy as np
import asyncio
import json
import time
import logging
import uuid
from typing import Union, Sequence


from storage import HeapPersistentStorage

class lat:
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
            self.xxdiv=45698
            self.xxpow=1.5
            self.xdiv = 456
            self.add=23
        elif self.protocol == 'coap':
            self.xxdiv=466
            self.xxpow=1.05
            self.xmul = 0
            self.add=15
        elif self.protocol == 'http':
            self.xxdiv=45997
            self.xxpow=1.53
            self.xmul = 7
            self.xdiv=45997
            self.add= 323/45997+32
        elif self.protocol == 'smqtt':
            self.xxdiv=74598765
            self.xxpow=2
            self.xdiv = 123
            self.add=17
        elif self.protocol == 'dds':
            self.xxmul=0
            self.xdiv = 10536
            self.xmul=11
            self.add=263
        lat= self.xxmul*(self.ln**self.xxpow+self.xxadd)/self.xxdiv +self.xmul*(self.ln+self.xadd)/self.xdiv+self.add

        time.sleep(self.ln/9000)
        return lat;
 
        
    