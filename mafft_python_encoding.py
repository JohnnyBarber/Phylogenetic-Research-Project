# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:01:49 2018

@author: Jiaqi Li
"""

import numpy
from scipy import *
import Bio
from Bio.Align.Applications import MafftCommandline

a = linspace(1,100,100)

i = 0
while i < 100:
    print('Now running sample%d' %(a[i]))
    mafft_exe = "D:\\MAFFT\\mafft-7.380-win64-signed\\mafft-win\\mafft.bat"
    in_file = "D:\\Research\\100_samples\\100_samples\\sample_shuffle_again%d.txt" %(a[i])
    mafft_cline = MafftCommandline(mafft_exe, input=in_file)
    print(mafft_cline)
    stdout, stderr = mafft_cline()
    with open("aligned_sample_shuffled%d.fasta" %(a[i]), "w") as handle:
        handle.write(stdout)
    from Bio import AlignIO
    align = AlignIO.read("aligned_sample_shuffled%d.fasta" %(a[i]), "fasta")
    i += 1