#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:22:27 2020

@author: danny
"""

import pandas as pd
import numpy as np

f = open('outputFile.txt', 'w')
data = pd.read_csv('reference list.csv')
bibtex = data['Bibtex']
for bib in bibtex.iteritems():
    if not pd.isnull(bib[1]):    
        f.write(bib[1])
        f.write('\n' * 2)
f.close()