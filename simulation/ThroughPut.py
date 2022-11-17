# -*- coding: utf-8 -*-

import numpy as np
import asyncio
import json

import logging
import uuid
from typing import Union, Sequence


from storage import HeapPersistentStorage

class Throughput:
    def __init__(self,protocol,msg_size):
        self.protocol=protocol
        self.ln=msg_size;
        self.xpow =1
        self.xmul =1
        self.add =0
    def actual(self):
        if self.protocol == 'mqttsn':
            self.xmul =0.03

        elif self.protocol == 'coap':
            self.xpow=0.7
            self.add=6

        elif self.protocol == 'http':

            self.xmul = 0.063

        elif self.protocol == 'smqtt':

            self.xmul = 0.023
        elif self.protocol == 'dds':
            self.xpow=0.004

        lat= self.ln-self.xmul*(self.ln**self.xpow) +self.add

        return lat;
 
        
    