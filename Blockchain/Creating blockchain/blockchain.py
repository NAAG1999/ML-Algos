#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 02:21:03 2018

@author: nilesh
"""

#importing libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building a bc

class blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, preHash= '0', )
