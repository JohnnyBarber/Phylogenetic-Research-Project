# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:50:07 2018

@author: Jiaqi Li
"""

from scipy import *
from itertools import permutations
from numpy.random import permutation
import numpy

All = open('sample100.txt','r+')
line = All.readlines()

L = sum(1 for line in line)
l = L//2
M = chararray((l,2))
M = chararray(M.shape, itemsize=1000)
M[:] = 'NA'

i = 0
j = 0
while i < L:
    M[j,0] = line[i]
    M[j,1] = line[i+1]
    i += 2
    j += 1

srs = permutation(arange(l))
Rand = M[srs,:]
Rand = concatenate(Rand)

j = 0
file = open("random_sample1000.txt","w")
while j < len(Rand):
    file.write("%s" %Rand[j].decode('utf-8') + '\n')
    j += 1
file.close()