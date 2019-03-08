# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:56:59 2018

@author: Jiaqi Li
"""

import scipy
import numpy
import random

data = open('seqs.txt','r+')
line = data.readlines()

L = sum(1 for line in line)
l = L//2

number1000 = random.sample(range(1,l),1000)
number2000 = random.sample(range(1,l),2000)
number100 = random.sample(range(1,l),100)

M = chararray((l,2))
M = chararray(M.shape,itemsize=1000)
M[:] = 'NA'
i = 0
j = 0
while i < L:
    M[j,0] = line[i]
    M[j,1] = line[i+1]
    i += 2
    j += 1

M1000 = chararray((1000,2))
M1000 = chararray(M1000.shape, itemsize=1000)
M1000[:] = 'NA'
M1000 = M[number1000,:]
M1000 = concatenate(M1000)

M2000 = chararray((2000,2))
M2000 = chararray(M2000.shape, itemsize=1000)
M2000[:] = 'NA'
M2000 = M[number2000,:]
M2000 = concatenate(M2000)

M100 = chararray((100,2))
M100 = chararray(M100.shape, itemsize=1000)
M100[:] = 'NA'
M100 = M[number100,:]
M100 = concatenate(M100)

sample = array([M1000,M2000,M100])

name = [1000,2000,100]
for i in range(3):
    file = open("sample%d.txt" %(name[i]),'w')
    j = 0
    while j < name[i]:
        file.write("%s" %(sample[i][j].decode('utf-8')) + '\n')
        j += 1
    file.close()
