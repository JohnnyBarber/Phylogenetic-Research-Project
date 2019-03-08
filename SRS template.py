# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:00:13 2018

@author: Jiaqi Li
"""
from scipy import *
import random
import numpy
from matplotlib.pyplot import *

#data----------------------------------
exp1 = open('seqs_101O.txt','r+')
line1 = exp1.readlines()
exp2 = open('seqs_102O.txt','r+')
line2 = exp2.readlines()
exp3 = open('seqs_103O.txt','r+')
line3 = exp3.readlines()
exp4 = open('seqs_104O.txt','r+')
line4 = exp4.readlines()
exp5 = open('seqs_105O.txt','r+')
line5 = exp5.readlines()
exp6 = open('seqs_106O.txt','r+')
line6 = exp6.readlines()
exp7 = open('seqs_107O.txt','r+')
line7 = exp7.readlines()
exp8 = open('seqs_108O.txt','r+')
line8 = exp8.readlines()
exp9 = open('seqs_109O.txt','r+')
line9 = exp9.readlines()
exp10 = open('seqs_110O.txt','r+')
line10 = exp10.readlines()
exp11 = open('seqs_111O.txt','r+')
line11 = exp11.readlines()
exp12 = open('seqs_112O.txt','r+')
line12 = exp12.readlines()
exp13 = open('seqs_113O.txt','r+')
line13 = exp13.readlines()
exp14 = open('seqs_114O.txt','r+')
line14 = exp14.readlines()
exp15 = open('seqs_115O.txt','r+')
line15 = exp15.readlines()
exp16 = open('seqs_116O.txt','r+')
line16 = exp16.readlines()
exp17 = open('seqs_117O.txt','r+')
line17 = exp17.readlines()
exp18 = open('seqs_118O.txt','r+')
line18 = exp18.readlines()
exp19 = open('seqs_119O.txt','r+')
line19 = exp19.readlines()
exp20 = open('seqs_120O.txt','r+')
line20 = exp20.readlines()
exp21 = open('seqs_121O.txt','r+')
line21 = exp21.readlines()
exp22 = open('seqs_122O.txt','r+')
line22 = exp22.readlines()
exp23 = open('seqs_123O.txt','r+')
line23 = exp23.readlines()
exp24 = open('seqs_124O.txt','r+')
line24 = exp24.readlines()
exp25 = open('seqs_125O.txt','r+')
line25 = exp25.readlines()
exp26 = open('seqs_201OW.txt','r+')
line26 = exp26.readlines()
exp27 = open('seqs_202OW.txt','r+')
line27 = exp27.readlines()
exp28 = open('seqs_203OW.txt','r+')
line28 = exp28.readlines()
exp29 = open('seqs_204OW.txt','r+')
line29 = exp29.readlines()
exp30 = open('seqs_205OW.txt','r+')
line30 = exp30.readlines()
exp31 = open('seqs_206OW.txt','r+')
line31 = exp31.readlines()
exp32 = open('seqs_207OW.txt','r+')
line32 = exp32.readlines()
exp33 = open('seqs_208OW.txt','r+')
line33 = exp33.readlines()
exp34 = open('seqs_209OW.txt','r+')
line34 = exp34.readlines()
exp35 = open('seqs_210OW.txt','r+')
line35 = exp35.readlines()
exp36 = open('seqs_211OW.txt','r+')
line36 = exp36.readlines()
exp37 = open('seqs_212OW.txt','r+')
line37 = exp37.readlines()
exp38 = open('seqs_213OW.txt','r+')
line38 = exp38.readlines()
exp39 = open('seqs_214OW.txt','r+')
line39 = exp39.readlines()
exp40 = open('seqs_215OW.txt','r+')
line40 = exp40.readlines()
exp41 = open('seqs_216OW.txt','r+')
line41 = exp41.readlines()
exp42 = open('seqs_217OW.txt','r+')
line42 = exp42.readlines()
exp43 = open('seqs_218OW.txt','r+')
line43 = exp43.readlines()
exp44 = open('seqs_219OW.txt','r+')
line44 = exp44.readlines()
exp45 = open('seqs_220OW.txt','r+')
line45 = exp45.readlines()
exp46 = open('seqs_221OW.txt','r+')
line46 = exp46.readlines()
exp47 = open('seqs_222OW.txt','r+')
line47 = exp47.readlines()
exp48 = open('seqs_223OW.txt','r+')
line48 = exp48.readlines()
exp49 = open('seqs_224OW.txt','r+')
line49 = exp49.readlines()
exp50 = open('seqs_225OW.txt','r+')
line50 = exp50.readlines()
exp51 = open('seqs_301C.txt','r+')
line51 = exp51.readlines()
exp52 = open('seqs_302C.txt','r+')
line52 = exp52.readlines()
exp53 = open('seqs_303C.txt','r+')
line53 = exp53.readlines()
exp54 = open('seqs_304C.txt','r+')
line54 = exp54.readlines()
exp55 = open('seqs_305C.txt','r+')
line55 = exp55.readlines()
exp56 = open('seqs_306C.txt','r+')
line56 = exp56.readlines()
exp57 = open('seqs_307C.txt','r+')
line57 = exp57.readlines()
exp58 = open('seqs_308C.txt','r+')
line58 = exp58.readlines()
exp59 = open('seqs_309C.txt','r+')
line59 = exp59.readlines()
exp60 = open('seqs_310C.txt','r+')
line60 = exp60.readlines()
exp61 = open('seqs_311C.txt','r+')
line61 = exp61.readlines()
exp62 = open('seqs_312C.txt','r+')
line62 = exp62.readlines()
exp63 = open('seqs_313C.txt','r+')
line63 = exp63.readlines()
exp64 = open('seqs_314C.txt','r+')
line64 = exp64.readlines()
exp65 = open('seqs_315C.txt','r+')
line65 = exp65.readlines()
exp66 = open('seqs_316C.txt','r+')
line66 = exp66.readlines()
exp67 = open('seqs_317C.txt','r+')
line67 = exp67.readlines()
exp68 = open('seqs_318C.txt','r+')
line68 = exp68.readlines()
exp69 = open('seqs_319C.txt','r+')
line69 = exp69.readlines()
exp70 = open('seqs_320C.txt','r+')
line70 = exp70.readlines()
exp71 = open('seqs_321C.txt','r+')
line71 = exp71.readlines()
exp72 = open('seqs_322C.txt','r+')
line72 = exp72.readlines()
exp73 = open('seqs_323C.txt','r+')
line73 = exp73.readlines()
exp74 = open('seqs_325C.txt','r+')
line74 = exp74.readlines()

#exp-----------------------------------
L1 = sum(1 for line in line1)
l1 = L1//2
M1 = chararray((l1,2))
M1 = chararray(M1.shape, itemsize=600)
M1[:] = 'NA'

L2 = sum(1 for line in line2)
l2 = L2//2
M2 = chararray((l2,2))
M2 = chararray(M2.shape, itemsize=600)
M2[:] = 'NA'

L3 = sum(1 for line in line3)
l3 = L3//2
M3 = chararray((l3,2))
M3 = chararray(M3.shape, itemsize=600)
M3[:] = 'NA'

L4 = sum(1 for line in line4)
l4 = L4//2
M4 = chararray((l4,2))
M4 = chararray(M4.shape, itemsize=600)
M4[:] = 'NA'

L5 = sum(1 for line in line5)
l5 = L5//2
M5 = chararray((l5,2))
M5 = chararray(M5.shape, itemsize=600)
M5[:] = 'NA'

L6 = sum(1 for line in line6)
l6 = L6//2
M6 = chararray((l6,2))
M6 = chararray(M6.shape, itemsize=600)
M6[:] = 'NA'

L7 = sum(1 for line in line7)
l7 = L7//2
M7 = chararray((l7,2))
M7 = chararray(M7.shape, itemsize=600)
M7[:] = 'NA'

L8 = sum(1 for line in line8)
l8 = L8//2
M8 = chararray((l8,2))
M8 = chararray(M8.shape, itemsize=600)
M8[:] = 'NA'

L9 = sum(1 for line in line9)
l9 = L9//2
M9 = chararray((l9,2))
M9 = chararray(M9.shape, itemsize=600)
M9[:] = 'NA'

L10 = sum(1 for line in line10)
l10 = L10//2
M10 = chararray((l10,2))
M10 = chararray(M10.shape, itemsize=600)
M10[:] = 'NA'

L11 = sum(1 for line in line11)
l11 = L11//2
M11 = chararray((l11,2))
M11 = chararray(M11.shape, itemsize=600)
M11[:] = 'NA'

L12 = sum(1 for line in line12)
l12 = L12//2
M12 = chararray((l12,2))
M12 = chararray(M12.shape, itemsize=600)
M12[:] = 'NA'

L13 = sum(1 for line in line13)
l13 = L13//2
M13 = chararray((l13,2))
M13 = chararray(M13.shape, itemsize=600)
M13[:] = 'NA'

L14 = sum(1 for line in line14)
l14 = L14//2
M14 = chararray((l14,2))
M14 = chararray(M14.shape, itemsize=600)
M14[:] = 'NA'

L15 = sum(1 for line in line15)
l15 = L15//2
M15 = chararray((l15,2))
M15 = chararray(M15.shape, itemsize=600)
M15[:] = 'NA'

L16 = sum(1 for line in line16)
l16 = L16//2
M16 = chararray((l16,2))
M16 = chararray(M16.shape, itemsize=600)
M16[:] = 'NA'

L17 = sum(1 for line in line17)
l17 = L17//2
M17 = chararray((l17,2))
M17 = chararray(M17.shape, itemsize=600)
M17[:] = 'NA'

L18 = sum(1 for line in line18)
l18 = L18//2
M18 = chararray((l18,2))
M18 = chararray(M18.shape, itemsize=600)
M18[:] = 'NA'

L19 = sum(1 for line in line19)
l19 = L19//2
M19 = chararray((l19,2))
M19 = chararray(M19.shape, itemsize=600)
M19[:] = 'NA'

L20 = sum(1 for line in line20)
l20 = L20//2
M20 = chararray((l20,2))
M20 = chararray(M20.shape, itemsize=600)
M20[:] = 'NA'

L21 = sum(1 for line in line21)
l21 = L21//2
M21 = chararray((l21,2))
M21 = chararray(M21.shape, itemsize=600)
M21[:] = 'NA'

L22 = sum(1 for line in line22)
l22 = L22//2
M22 = chararray((l22,2))
M22 = chararray(M22.shape, itemsize=600)
M22[:] = 'NA'

L23 = sum(1 for line in line23)
l23 = L23//2
M23 = chararray((l23,2))
M23 = chararray(M23.shape, itemsize=600)
M23[:] = 'NA'

L24 = sum(1 for line in line24)
l24 = L24//2
M24 = chararray((l24,2))
M24 = chararray(M24.shape, itemsize=600)
M24[:] = 'NA'

L25 = sum(1 for line in line25)
l25 = L25//2
M25 = chararray((l25,2))
M25 = chararray(M25.shape, itemsize=600)
M25[:] = 'NA'

L26 = sum(1 for line in line26)
l26 = L26//2
M26 = chararray((l26,2))
M26 = chararray(M26.shape, itemsize=600)
M26[:] = 'NA'

L27 = sum(1 for line in line27)
l27 = L27//2
M27 = chararray((l27,2))
M27 = chararray(M27.shape, itemsize=600)
M27[:] = 'NA'

L28 = sum(1 for line in line28)
l28 = L28//2
M28 = chararray((l28,2))
M28 = chararray(M28.shape, itemsize=600)
M28[:] = 'NA'

L29 = sum(1 for line in line29)
l29 = L29//2
M29 = chararray((l29,2))
M29 = chararray(M29.shape, itemsize=600)
M29[:] = 'NA'

L30 = sum(1 for line in line30)
l30 = L30//2
M30 = chararray((l30,2))
M30 = chararray(M30.shape, itemsize=600)
M30[:] = 'NA'

L31 = sum(1 for line in line13)
l31 = L31//2
M31 = chararray((l31,2))
M31 = chararray(M31.shape, itemsize=600)
M31[:] = 'NA'

L32 = sum(1 for line in line32)
l32 = L32//2
M32 = chararray((l32,2))
M32 = chararray(M32.shape, itemsize=600)
M32[:] = 'NA'

L33 = sum(1 for line in line33)
l33 = L33//2
M33 = chararray((l33,2))
M33 = chararray(M33.shape, itemsize=600)
M33[:] = 'NA'

L34 = sum(1 for line in line34)
l34 = L34//2
M34 = chararray((l34,2))
M34 = chararray(M34.shape, itemsize=600)
M34[:] = 'NA'

L35 = sum(1 for line in line35)
l35 = L35//2
M35 = chararray((l35,2))
M35 = chararray(M35.shape, itemsize=600)
M35[:] = 'NA'

L36 = sum(1 for line in line36)
l36 = L36//2
M36 = chararray((l36,2))
M36 = chararray(M36.shape, itemsize=600)
M36[:] = 'NA'

L37 = sum(1 for line in line37)
l37 = L37//2
M37 = chararray((l37,2))
M37 = chararray(M37.shape, itemsize=600)
M37[:] = 'NA'

L38 = sum(1 for line in line38)
l38 = L38//2
M38 = chararray((l38,2))
M38 = chararray(M38.shape, itemsize=600)
M38[:] = 'NA'

L39 = sum(1 for line in line39)
l39 = L39//2
M39 = chararray((l39,2))
M39 = chararray(M39.shape, itemsize=600)
M39[:] = 'NA'

L40 = sum(1 for line in line40)
l40 = L40//2
M40 = chararray((l40,2))
M40 = chararray(M40.shape, itemsize=600)
M40[:] = 'NA'

L41 = sum(1 for line in line41)
l41 = L41//2
M41 = chararray((l41,2))
M41 = chararray(M41.shape, itemsize=600)
M41[:] = 'NA'

L42 = sum(1 for line in line42)
l42 = L42//2
M42 = chararray((l42,2))
M42 = chararray(M42.shape, itemsize=600)
M42[:] = 'NA'

L43 = sum(1 for line in line43)
l43 = L43//2
M43 = chararray((l43,2))
M43 = chararray(M43.shape, itemsize=600)
M43[:] = 'NA'

L44 = sum(1 for line in line44)
l44 = L44//2
M44 = chararray((l44,2))
M44 = chararray(M44.shape, itemsize=600)
M44[:] = 'NA'

L45 = sum(1 for line in line45)
l45 = L45//2
M45 = chararray((l45,2))
M45 = chararray(M45.shape, itemsize=600)
M45[:] = 'NA'

L46 = sum(1 for line in line46)
l46 = L46//2
M46 = chararray((l46,2))
M46 = chararray(M46.shape, itemsize=600)
M46[:] = 'NA'

L47 = sum(1 for line in line47)
l47 = L47//2
M47 = chararray((l47,2))
M47 = chararray(M47.shape, itemsize=600)
M47[:] = 'NA'

L48 = sum(1 for line in line48)
l48 = L48//2
M48 = chararray((l48,2))
M48 = chararray(M48.shape, itemsize=600)
M48[:] = 'NA'

L49 = sum(1 for line in line49)
l49 = L49//2
M49 = chararray((l49,2))
M49 = chararray(M49.shape, itemsize=600)
M49[:] = 'NA'

L50 = sum(1 for line in line50)
l50 = L50//2
M50 = chararray((l50,2))
M50 = chararray(M50.shape, itemsize=600)
M50[:] = 'NA'

L51 = sum(1 for line in line51)
l51 = L51//2
M51 = chararray((l51,2))
M51 = chararray(M51.shape, itemsize=600)
M51[:] = 'NA'

L52 = sum(1 for line in line52)
l52 = L52//2
M52 = chararray((l52,2))
M52 = chararray(M52.shape, itemsize=600)
M52[:] = 'NA'

L53 = sum(1 for line in line53)
l53 = L53//2
M53 = chararray((l53,2))
M53 = chararray(M53.shape, itemsize=600)
M53[:] = 'NA'

L54 = sum(1 for line in line54)
l54 = L54//2
M54 = chararray((l54,2))
M54 = chararray(M54.shape, itemsize=600)
M54[:] = 'NA'

L55 = sum(1 for line in line55)
l55 = L55//2
M55 = chararray((l55,2))
M55 = chararray(M55.shape, itemsize=600)
M55[:] = 'NA'

L56 = sum(1 for line in line56)
l56 = L56//2
M56 = chararray((l56,2))
M56 = chararray(M56.shape, itemsize=600)
M56[:] = 'NA'

L57 = sum(1 for line in line57)
l57 = L57//2
M57 = chararray((l57,2))
M57 = chararray(M57.shape, itemsize=600)
M57[:] = 'NA'

L58 = sum(1 for line in line58)
l58 = L58//2
M58 = chararray((l58,2))
M58 = chararray(M58.shape, itemsize=600)
M58[:] = 'NA'

L59 = sum(1 for line in line59)
l59 = L59//2
M59 = chararray((l59,2))
M59 = chararray(M59.shape, itemsize=600)
M59[:] = 'NA'

L60 = sum(1 for line in line60)
l60 = L60//2
M60 = chararray((l60,2))
M60 = chararray(M60.shape, itemsize=600)
M60[:] = 'NA'

L61 = sum(1 for line in line61)
l61 = L61//2
M61 = chararray((l61,2))
M61 = chararray(M61.shape, itemsize=600)
M61[:] = 'NA'

L62 = sum(1 for line in line62)
l62 = L62//2
M62 = chararray((l62,2))
M62 = chararray(M62.shape, itemsize=600)
M62[:] = 'NA'

L63 = sum(1 for line in line63)
l63 = L63//2
M63 = chararray((l63,2))
M63 = chararray(M63.shape, itemsize=600)
M63[:] = 'NA'

L64 = sum(1 for line in line64)
l64 = L64//2
M64 = chararray((l64,2))
M64 = chararray(M64.shape, itemsize=600)
M64[:] = 'NA'

L65 = sum(1 for line in line65)
l65 = L65//2
M65 = chararray((l65,2))
M65 = chararray(M65.shape, itemsize=600)
M65[:] = 'NA'

L66 = sum(1 for line in line66)
l66 = L66//2
M66 = chararray((l66,2))
M66 = chararray(M66.shape, itemsize=600)
M66[:] = 'NA'

L67 = sum(1 for line in line67)
l67 = L67//2
M67 = chararray((l67,2))
M67 = chararray(M67.shape, itemsize=600)
M67[:] = 'NA'

L68 = sum(1 for line in line68)
l68 = L68//2
M68 = chararray((l68,2))
M68 = chararray(M68.shape, itemsize=600)
M68[:] = 'NA'

L69 = sum(1 for line in line69)
l69 = L69//2
M69 = chararray((l69,2))
M69 = chararray(M69.shape, itemsize=600)
M69[:] = 'NA'

L70 = sum(1 for line in line70)
l70 = L70//2
M70 = chararray((l70,2))
M70 = chararray(M70.shape, itemsize=600)
M70[:] = 'NA'

L71 = sum(1 for line in line71)
l71 = L71//2
M71 = chararray((l71,2))
M71 = chararray(M71.shape, itemsize=600)
M71[:] = 'NA'

L72 = sum(1 for line in line72)
l72 = L72//2
M72 = chararray((l72,2))
M72 = chararray(M72.shape, itemsize=600)
M72[:] = 'NA'

L73 = sum(1 for line in line73)
l73 = L73//2
M73 = chararray((l73,2))
M73 = chararray(M73.shape, itemsize=600)
M73[:] = 'NA'

L74 = sum(1 for line in line74)
l74 = L74//2
M74 = chararray((l74,2))
M74 = chararray(M74.shape, itemsize=600)
M74[:] = 'NA'

#strategy------------------------------
i = 0
j = 0
while i < L1:
    M1[j,0] = line1[i]
    M1[j,1] = line1[i+1]
    i += 2
    j += 1
    
i = 0
j = 0
while i < L2:
    M2[j,0] = line2[i]
    M2[j,1] = line2[i+1]
    i += 2
    j += 1
    
i = 0
j = 0
while i < L3:
    M3[j,0] = line3[i]
    M3[j,1] = line3[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L4:
    M4[j,0] = line4[i]
    M4[j,1] = line4[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L5:
    M5[j,0] = line5[i]
    M5[j,1] = line5[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L6:
    M6[j,0] = line6[i]
    M6[j,1] = line6[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L7:
    M7[j,0] = line7[i]
    M7[j,1] = line7[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L8:
    M8[j,0] = line8[i]
    M8[j,1] = line8[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L9:
    M9[j,0] = line9[i]
    M9[j,1] = line9[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L10:
    M10[j,0] = line10[i]
    M10[j,1] = line10[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L11:
    M11[j,0] = line11[i]
    M11[j,1] = line11[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L12:
    M12[j,0] = line12[i]
    M12[j,1] = line12[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L13:
    M13[j,0] = line13[i]
    M13[j,1] = line13[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L14:
    M14[j,0] = line14[i]
    M14[j,1] = line14[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L15:
    M15[j,0] = line15[i]
    M15[j,1] = line15[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L16:
    M16[j,0] = line16[i]
    M16[j,1] = line16[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L17:
    M17[j,0] = line17[i]
    M17[j,1] = line17[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L18:
    M18[j,0] = line18[i]
    M18[j,1] = line18[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L19:
    M19[j,0] = line19[i]
    M19[j,1] = line19[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L20:
    M20[j,0] = line20[i]
    M20[j,1] = line20[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L21:
    M21[j,0] = line21[i]
    M21[j,1] = line21[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L22:
    M22[j,0] = line22[i]
    M22[j,1] = line22[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L23:
    M23[j,0] = line23[i]
    M23[j,1] = line23[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L24:
    M24[j,0] = line24[i]
    M24[j,1] = line24[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L25:
    M25[j,0] = line25[i]
    M25[j,1] = line25[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L26:
    M26[j,0] = line26[i]
    M26[j,1] = line26[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L27:
    M27[j,0] = line27[i]
    M27[j,1] = line27[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L28:
    M28[j,0] = line28[i]
    M28[j,1] = line28[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L29:
    M29[j,0] = line29[i]
    M29[j,1] = line29[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L30:
    M30[j,0] = line30[i]
    M30[j,1] = line30[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L31:
    M31[j,0] = line31[i]
    M31[j,1] = line31[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L32:
    M32[j,0] = line32[i]
    M32[j,1] = line32[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L33:
    M33[j,0] = line33[i]
    M33[j,1] = line33[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L34:
    M34[j,0] = line34[i]
    M34[j,1] = line34[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L35:
    M35[j,0] = line35[i]
    M35[j,1] = line35[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L36:
    M36[j,0] = line36[i]
    M36[j,1] = line36[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L37:
    M37[j,0] = line37[i]
    M37[j,1] = line37[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L38:
    M38[j,0] = line38[i]
    M38[j,1] = line38[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L39:
    M39[j,0] = line39[i]
    M39[j,1] = line39[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L40:
    M40[j,0] = line40[i]
    M40[j,1] = line40[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L41:
    M41[j,0] = line41[i]
    M41[j,1] = line41[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L42:
    M42[j,0] = line42[i]
    M42[j,1] = line42[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L43:
    M43[j,0] = line43[i]
    M43[j,1] = line43[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L44:
    M44[j,0] = line44[i]
    M44[j,1] = line44[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L45:
    M45[j,0] = line45[i]
    M45[j,1] = line45[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L46:
    M46[j,0] = line46[i]
    M46[j,1] = line46[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L47:
    M47[j,0] = line47[i]
    M47[j,1] = line47[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L48:
    M48[j,0] = line48[i]
    M48[j,1] = line48[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L49:
    M49[j,0] = line49[i]
    M49[j,1] = line49[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L50:
    M50[j,0] = line50[i]
    M50[j,1] = line50[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L51:
    M51[j,0] = line51[i]
    M51[j,1] = line51[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L52:
    M52[j,0] = line52[i]
    M52[j,1] = line52[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L53:
    M53[j,0] = line53[i]
    M53[j,1] = line53[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L54:
    M54[j,0] = line54[i]
    M54[j,1] = line54[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L55:
    M55[j,0] = line55[i]
    M55[j,1] = line55[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L56:
    M56[j,0] = line56[i]
    M56[j,1] = line56[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L57:
    M57[j,0] = line57[i]
    M57[j,1] = line57[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L58:
    M58[j,0] = line58[i]
    M58[j,1] = line58[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L59:
    M59[j,0] = line59[i]
    M59[j,1] = line59[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L60:
    M60[j,0] = line60[i]
    M60[j,1] = line60[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L61:
    M61[j,0] = line61[i]
    M61[j,1] = line61[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L62:
    M62[j,0] = line62[i]
    M62[j,1] = line62[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L63:
    M63[j,0] = line63[i]
    M63[j,1] = line63[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L64:
    M64[j,0] = line64[i]
    M64[j,1] = line64[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L65:
    M56[j,0] = line65[i]
    M65[j,1] = line65[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L66:
    M66[j,0] = line66[i]
    M66[j,1] = line66[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L67:
    M67[j,0] = line67[i]
    M67[j,1] = line67[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L68:
    M68[j,0] = line68[i]
    M68[j,1] = line68[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L69:
    M69[j,0] = line69[i]
    M69[j,1] = line69[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L70:
    M70[j,0] = line70[i]
    M70[j,1] = line70[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L71:
    M71[j,0] = line71[i]
    M71[j,1] = line71[i+1]
    i += 2
    j += 1

i = 0
j = 0
while i < L72:
    M72[j,0] = line72[i]
    M72[j,1] = line72[i+1]
    i += 2
    j += 1
 
i = 0
j = 0
while i < L73:
    M73[j,0] = line73[i]
    M73[j,1] = line73[i+1]
    i += 2
    j += 1    

i = 0
j = 0
while i < L74:
    M74[j,0] = line74[i]
    M74[j,1] = line74[i+1]
    i += 2
    j += 1

#SRS-----------------------------------
size1 = range(0,l1)
pick1 = random.sample(size1,135)
sample1 = M1[pick1,:]

size2 = range(0,l2)
pick2 = random.sample(size2,135)
sample2 = M2[pick2,:]

size3 = range(0,l3)
pick3 = random.sample(size3,135)
sample3 = M3[pick3,:]

size4 = range(0,l4)
pick4 = random.sample(size4,135)
sample4 = M4[pick4,:]

size5 = range(0,l5)
pick5 = random.sample(size5,135)
sample5 = M5[pick5,:]

size6 = range(0,l6)
pick6 = random.sample(size6,135)
sample6 = M6[pick6,:]

size7 = range(0,l7)
pick7 = random.sample(size7,135)
sample7 = M7[pick7,:]

size8 = range(0,l8)
pick8 = random.sample(size8,135)
sample8 = M8[pick8,:]

size9 = range(0,l9)
pick9 = random.sample(size9,135)
sample9 = M9[pick9,:]

size10 = range(0,l10)
pick10 = random.sample(size10,135)
sample10 = M10[pick10,:]

size11 = range(0,l11)
pick11 = random.sample(size11,135)
sample11 = M11[pick11,:]

size12 = range(0,l12)
pick12 = random.sample(size12,135)
sample12 = M12[pick12,:]

size13 = range(0,l13)
pick13 = random.sample(size13,135)
sample13 = M13[pick13,:]

size14 = range(0,l14)
pick14 = random.sample(size14,135)
sample14 = M14[pick14,:]

size15 = range(0,l15)
pick15 = random.sample(size15,135)
sample15 = M15[pick15,:]

size16 = range(0,l16)
pick16 = random.sample(size16,135)
sample16 = M16[pick16,:]

size17 = range(0,l17)
pick17 = random.sample(size17,135)
sample17 = M17[pick17,:]

size18 = range(0,l18)
pick18 = random.sample(size18,135)
sample18 = M18[pick18,:]

size19 = range(0,l19)
pick19 = random.sample(size19,135)
sample19 = M19[pick19,:]

size20 = range(0,l20)
pick20 = random.sample(size20,135)
sample20 = M20[pick20,:]

size21 = range(0,l21)
pick21 = random.sample(size21,135)
sample21 = M21[pick21,:]

size22 = range(0,l22)
pick22 = random.sample(size22,135)
sample22 = M22[pick22,:]

size23 = range(0,l23)
pick23 = random.sample(size23,135)
sample23 = M23[pick23,:]

size24 = range(0,l24)
pick24 = random.sample(size24,135)
sample24 = M24[pick24,:]

size25 = range(0,l25)
pick25 = random.sample(size25,135)
sample25 = M25[pick25,:]

size26 = range(0,l26)
pick26 = random.sample(size26,135)
sample26 = M26[pick26,:]

size27 = range(0,l27)
pick27 = random.sample(size27,135)
sample27 = M27[pick27,:]

size28 = range(0,l28)
pick28 = random.sample(size28,135)
sample28 = M28[pick28,:]

size29 = range(0,l29)
pick29 = random.sample(size29,135)
sample29 = M29[pick29,:]

size30 = range(0,l30)
pick30 = random.sample(size30,135)
sample30 = M30[pick30,:]

size31 = range(0,l31)
pick31 = random.sample(size31,135)
sample31 = M31[pick31,:]

size32 = range(0,l32)
pick32 = random.sample(size32,135)
sample32 = M32[pick32,:]

size33 = range(0,l33)
pick33 = random.sample(size33,135)
sample33 = M33[pick33,:]

size34 = range(0,l34)
pick34 = random.sample(size34,135)
sample34 = M34[pick34,:]

size35 = range(0,l35)
pick35 = random.sample(size35,135)
sample35 = M35[pick35,:]

size36 = range(0,l36)
pick36 = random.sample(size36,135)
sample36 = M36[pick36,:]

size37 = range(0,l37)
pick37 = random.sample(size37,135)
sample37 = M37[pick37,:]

size38 = range(0,l38)
pick38 = random.sample(size38,135)
sample38 = M38[pick38,:]

size39 = range(0,l39)
pick39 = random.sample(size39,135)
sample39 = M39[pick39,:]

size40 = range(0,l40)
pick40 = random.sample(size40,135)
sample40 = M40[pick40,:]

size41 = range(0,l41)
pick41 = random.sample(size41,135)
sample41 = M41[pick41,:]

size42 = range(0,l42)
pick42 = random.sample(size42,135)
sample42 = M42[pick42,:]

size43 = range(0,l43)
pick43 = random.sample(size43,135)
sample43 = M43[pick43,:]

size44 = range(0,l44)
pick44 = random.sample(size44,135)
sample44 = M44[pick44,:]

size45 = range(0,l45)
pick45 = random.sample(size45,135)
sample45 = M45[pick45,:]

size46 = range(0,l46)
pick46 = random.sample(size46,135)
sample46 = M46[pick46,:]

size47 = range(0,l47)
pick47 = random.sample(size47,135)
sample47 = M47[pick47,:]

size48 = range(0,l48)
pick48 = random.sample(size48,135)
sample48 = M48[pick48,:]

size49 = range(0,l49)
pick49 = random.sample(size49,135)
sample49 = M49[pick49,:]

size50 = range(0,l50)
pick50 = random.sample(size50,135)
sample50 = M50[pick50,:]

size51 = range(0,l51)
pick51 = random.sample(size51,135)
sample51 = M51[pick51,:]

size52 = range(0,l52)
pick52 = random.sample(size52,135)
sample52 = M52[pick52,:]

size53 = range(0,l53)
pick53 = random.sample(size53,135)
sample53 = M53[pick53,:]

size54 = range(0,l54)
pick54 = random.sample(size54,135)
sample54 = M54[pick54,:]

size55 = range(0,l55)
pick55 = random.sample(size55,135)
sample55 = M55[pick55,:]

size56 = range(0,l56)
pick56 = random.sample(size56,135)
sample56 = M56[pick56,:]

size57 = range(0,l57)
pick57 = random.sample(size57,135)
sample57 = M57[pick57,:]

size58 = range(0,l58)
pick58 = random.sample(size58,135)
sample58 = M58[pick58,:]

size59 = range(0,l59)
pick59 = random.sample(size59,135)
sample59 = M59[pick59,:]

size60 = range(0,l60)
pick60 = random.sample(size60,135)
sample60 = M60[pick60,:]

size61 = range(0,l61)
pick61 = random.sample(size61,135)
sample61 = M61[pick61,:]

size62 = range(0,l62)
pick62 = random.sample(size62,135)
sample62 = M62[pick62,:]

size63 = range(0,l63)
pick63 = random.sample(size63,135)
sample63 = M63[pick63,:]

size64 = range(0,l64)
pick64 = random.sample(size64,135)
sample64 = M64[pick64,:]

size65 = range(0,l65)
pick65 = random.sample(size65,135)
sample65 = M65[pick65,:]

size66 = range(0,l66)
pick66 = random.sample(size66,135)
sample66 = M66[pick66,:]

size67 = range(0,l67)
pick67 = random.sample(size67,135)
sample67 = M67[pick67,:]

size68 = range(0,l68)
pick68 = random.sample(size68,135)
sample68 = M68[pick68,:]

size69 = range(0,l69)
pick69 = random.sample(size69,135)
sample69 = M69[pick69,:]

size70 = range(0,l70)
pick70 = random.sample(size70,135)
sample70 = M70[pick70,:]

size71 = range(0,l71)
pick71 = random.sample(size71,135)
sample71 = M71[pick71,:]

size72 = range(0,l72)
pick72 = random.sample(size72,135)
sample72 = M72[pick72,:]

size73 = range(0,l73)
pick73 = random.sample(size73,135)
sample73 = M73[pick73,:]

size74 = range(0,l74)
pick74 = random.sample(size74,135)
sample74 = M74[pick74,:]

#combine-------------------------------
Alls = []
Alls.append(sample1)
Alls.append(sample2)
Alls.append(sample3)
Alls.append(sample4)
Alls.append(sample5)
Alls.append(sample6)
Alls.append(sample7)
Alls.append(sample8)
Alls.append(sample9)
Alls.append(sample10)
Alls.append(sample11)
Alls.append(sample12)
Alls.append(sample13)
Alls.append(sample14)
Alls.append(sample15)
Alls.append(sample16)
Alls.append(sample17)
Alls.append(sample18)
Alls.append(sample19)
Alls.append(sample20)
Alls.append(sample21)
Alls.append(sample22)
Alls.append(sample23)
Alls.append(sample24)
Alls.append(sample25)
Alls.append(sample26)
Alls.append(sample27)
Alls.append(sample28)
Alls.append(sample29)
Alls.append(sample30)
Alls.append(sample31)
Alls.append(sample32)
Alls.append(sample33)
Alls.append(sample34)
Alls.append(sample35)
Alls.append(sample36)
Alls.append(sample37)
Alls.append(sample38)
Alls.append(sample39)
Alls.append(sample40)
Alls.append(sample41)
Alls.append(sample42)
Alls.append(sample43)
Alls.append(sample44)
Alls.append(sample45)
Alls.append(sample46)
Alls.append(sample47)
Alls.append(sample48)
Alls.append(sample49)
Alls.append(sample50)
Alls.append(sample51)
Alls.append(sample52)
Alls.append(sample53)
Alls.append(sample54)
Alls.append(sample55)
Alls.append(sample56)
Alls.append(sample57)
Alls.append(sample58)
Alls.append(sample59)
Alls.append(sample60)
Alls.append(sample61)
Alls.append(sample62)
Alls.append(sample63)
Alls.append(sample64)
Alls.append(sample65)
Alls.append(sample66)
Alls.append(sample67)
Alls.append(sample68)
Alls.append(sample69)
Alls.append(sample70)
Alls.append(sample71)
Alls.append(sample72)
Alls.append(sample73)
Alls.append(sample74)

#seperated plots-----------------------
"transf = zeros((135))"
"k = 0"
"while k < 135:"
"    transf[k] = len(sample[k,1])"
"    k += 1"
"scale = range(0,135)"
"plot(scale,transf)"
"Above may not be needed."

#combine plots-------------------------
p1 = zeros((135))
k = 0
while k < 135:
    p1[k] = len(sample1[k,1])
    k += 1

p2 = zeros((135))
k = 0
while k < 135:
    p2[k] = len(sample2[k,1])
    k += 1

p3 = zeros((135))
k = 0
while k < 135:
    p3[k] = len(sample3[k,1])
    k += 1

p4 = zeros((135))
k = 0
while k < 135:
    p4[k] = len(sample4[k,1])
    k += 1

p5 = zeros((135))
k = 0
while k < 135:
    p5[k] = len(sample5[k,1])
    k += 1

p6 = zeros((135))
k = 0
while k < 135:
    p6[k] = len(sample6[k,1])
    k += 1

p7 = zeros((135))
k = 0
while k < 135:
    p7[k] = len(sample7[k,1])
    k += 1

p8 = zeros((135))
k = 0
while k < 135:
    p8[k] = len(sample8[k,1])
    k += 1

p9 = zeros((135))
k = 0
while k < 135:
    p9[k] = len(sample9[k,1])
    k += 1

p10 = zeros((135))
k = 0
while k < 135:
    p10[k] = len(sample10[k,1])
    k += 1

p11 = zeros((135))
k = 0
while k < 135:
    p11[k] = len(sample11[k,1])
    k += 1

p12 = zeros((135))
k = 0
while k < 135:
    p12[k] = len(sample12[k,1])
    k += 1

p13 = zeros((135))
k = 0
while k < 135:
    p13[k] = len(sample13[k,1])
    k += 1

p14 = zeros((135))
k = 0
while k < 135:
    p14[k] = len(sample14[k,1])
    k += 1

p15 = zeros((135))
k = 0
while k < 135:
    p15[k] = len(sample15[k,1])
    k += 1

p16 = zeros((135))
k = 0
while k < 135:
    p16[k] = len(sample16[k,1])
    k += 1

p17 = zeros((135))
k = 0
while k < 135:
    p17[k] = len(sample17[k,1])
    k += 1

p18 = zeros((135))
k = 0
while k < 135:
    p18[k] = len(sample18[k,1])
    k += 1

p19 = zeros((135))
k = 0
while k < 135:
    p19[k] = len(sample19[k,1])
    k += 1

p20 = zeros((135))
k = 0
while k < 135:
    p20[k] = len(sample20[k,1])
    k += 1

p21 = zeros((135))
k = 0
while k < 135:
    p21[k] = len(sample21[k,1])
    k += 1

p22 = zeros((135))
k = 0
while k < 135:
    p22[k] = len(sample22[k,1])
    k += 1

p23 = zeros((135))
k = 0
while k < 135:
    p23[k] = len(sample23[k,1])
    k += 1

p24 = zeros((135))
k = 0
while k < 135:
    p24[k] = len(sample24[k,1])
    k += 1

p25 = zeros((135))
k = 0
while k < 135:
    p25[k] = len(sample25[k,1])
    k += 1

p26 = zeros((135))
k = 0
while k < 135:
    p26[k] = len(sample26[k,1])
    k += 1

p27 = zeros((135))
k = 0
while k < 135:
    p27[k] = len(sample27[k,1])
    k += 1

p28 = zeros((135))
k = 0
while k < 135:
    p28[k] = len(sample28[k,1])
    k += 1

p29 = zeros((135))
k = 0
while k < 135:
    p29[k] = len(sample29[k,1])
    k += 1

p30 = zeros((135))
k = 0
while k < 135:
    p30[k] = len(sample30[k,1])
    k += 1

p31 = zeros((135))
k = 0
while k < 135:
    p31[k] = len(sample31[k,1])
    k += 1

p32 = zeros((135))
k = 0
while k < 135:
    p32[k] = len(sample32[k,1])
    k += 1

p33 = zeros((135))
k = 0
while k < 135:
    p33[k] = len(sample33[k,1])
    k += 1

p34 = zeros((135))
k = 0
while k < 135:
    p34[k] = len(sample34[k,1])
    k += 1

p35 = zeros((135))
k = 0
while k < 135:
    p35[k] = len(sample35[k,1])
    k += 1

p36 = zeros((135))
k = 0
while k < 135:
    p36[k] = len(sample36[k,1])
    k += 1

p37 = zeros((135))
k = 0
while k < 135:
    p37[k] = len(sample37[k,1])
    k += 1

p38 = zeros((135))
k = 0
while k < 135:
    p38[k] = len(sample38[k,1])
    k += 1

p39 = zeros((135))
k = 0
while k < 135:
    p39[k] = len(sample39[k,1])
    k += 1

p40 = zeros((135))
k = 0
while k < 135:
    p40[k] = len(sample40[k,1])
    k += 1

p41 = zeros((135))
k = 0
while k < 135:
    p41[k] = len(sample41[k,1])
    k += 1

p42 = zeros((135))
k = 0
while k < 135:
    p42[k] = len(sample42[k,1])
    k += 1

p43 = zeros((135))
k = 0
while k < 135:
    p43[k] = len(sample43[k,1])
    k += 1

p44 = zeros((135))
k = 0
while k < 135:
    p44[k] = len(sample44[k,1])
    k += 1

p45 = zeros((135))
k = 0
while k < 135:
    p45[k] = len(sample45[k,1])
    k += 1

p46 = zeros((135))
k = 0
while k < 135:
    p46[k] = len(sample46[k,1])
    k += 1

p47 = zeros((135))
k = 0
while k < 135:
    p47[k] = len(sample47[k,1])
    k += 1

p48 = zeros((135))
k = 0
while k < 135:
    p48[k] = len(sample48[k,1])
    k += 1

p49 = zeros((135))
k = 0
while k < 135:
    p49[k] = len(sample49[k,1])
    k += 1

p50 = zeros((135))
k = 0
while k < 135:
    p50[k] = len(sample50[k,1])
    k += 1

p51 = zeros((135))
k = 0
while k < 135:
    p51[k] = len(sample51[k,1])
    k += 1

p52 = zeros((135))
k = 0
while k < 135:
    p52[k] = len(sample52[k,1])
    k += 1

p53 = zeros((135))
k = 0
while k < 135:
    p53[k] = len(sample53[k,1])
    k += 1

p54 = zeros((135))
k = 0
while k < 135:
    p54[k] = len(sample54[k,1])
    k += 1

p55 = zeros((135))
k = 0
while k < 135:
    p55[k] = len(sample55[k,1])
    k += 1

p56 = zeros((135))
k = 0
while k < 135:
    p56[k] = len(sample56[k,1])
    k += 1

p57 = zeros((135))
k = 0
while k < 135:
    p57[k] = len(sample57[k,1])
    k += 1

p58 = zeros((135))
k = 0
while k < 135:
    p58[k] = len(sample58[k,1])
    k += 1

p59 = zeros((135))
k = 0
while k < 135:
    p59[k] = len(sample59[k,1])
    k += 1

p60 = zeros((135))
k = 0
while k < 135:
    p60[k] = len(sample60[k,1])
    k += 1

p61 = zeros((135))
k = 0
while k < 135:
    p61[k] = len(sample61[k,1])
    k += 1

p62 = zeros((135))
k = 0
while k < 135:
    p62[k] = len(sample62[k,1])
    k += 1

p63 = zeros((135))
k = 0
while k < 135:
    p63[k] = len(sample63[k,1])
    k += 1

p64 = zeros((135))
k = 0
while k < 135:
    p64[k] = len(sample64[k,1])
    k += 1

p65 = zeros((135))
k = 0
while k < 135:
    p65[k] = len(sample65[k,1])
    k += 1

p66 = zeros((135))
k = 0
while k < 135:
    p66[k] = len(sample66[k,1])
    k += 1

p67 = zeros((135))
k = 0
while k < 135:
    p67[k] = len(sample67[k,1])
    k += 1

p68 = zeros((135))
k = 0
while k < 135:
    p68[k] = len(sample68[k,1])
    k += 1

p69 = zeros((135))
k = 0
while k < 135:
    p69[k] = len(sample69[k,1])
    k += 1

p70 = zeros((135))
k = 0
while k < 135:
    p70[k] = len(sample70[k,1])
    k += 1

p71 = zeros((135))
k = 0
while k < 135:
    p71[k] = len(sample71[k,1])
    k += 1

p72 = zeros((135))
k = 0
while k < 135:
    p72[k] = len(sample72[k,1])
    k += 1

p73 = zeros((135))
k = 0
while k < 135:
    p73[k] = len(sample73[k,1])
    k += 1

p74 = zeros((135))
k = 0
while k < 135:
    p74[k] = len(sample74[k,1])
    k += 1

p = []
p.extend(p1[:])
p.extend(p2[:])
p.extend(p3[:])
p.extend(p4[:])
p.extend(p5[:])
p.extend(p6[:])
p.extend(p7[:])
p.extend(p8[:])
p.extend(p9[:])
p.extend(p10[:])
p.extend(p11[:])
p.extend(p12[:])
p.extend(p13[:])
p.extend(p14[:])
p.extend(p15[:])
p.extend(p16[:])
p.extend(p17[:])
p.extend(p18[:])
p.extend(p19[:])
p.extend(p20[:])
p.extend(p21[:])
p.extend(p22[:])
p.extend(p23[:])
p.extend(p24[:])
p.extend(p25[:])
p.extend(p26[:])
p.extend(p27[:])
p.extend(p28[:])
p.extend(p29[:])
p.extend(p30[:])
p.extend(p31[:])
p.extend(p32[:])
p.extend(p33[:])
p.extend(p34[:])
p.extend(p35[:])
p.extend(p36[:])
p.extend(p37[:])
p.extend(p38[:])
p.extend(p39[:])
p.extend(p40[:])
p.extend(p41[:])
p.extend(p42[:])
p.extend(p43[:])
p.extend(p44[:])
p.extend(p45[:])
p.extend(p46[:])
p.extend(p47[:])
p.extend(p48[:])
p.extend(p49[:])
p.extend(p50[:])
p.extend(p51[:])
p.extend(p52[:])
p.extend(p53[:])
p.extend(p54[:])
p.extend(p55[:])
p.extend(p56[:])
p.extend(p57[:])
p.extend(p58[:])
p.extend(p59[:])
p.extend(p60[:])
p.extend(p61[:])
p.extend(p62[:])
p.extend(p63[:])
p.extend(p64[:])
p.extend(p65[:])
p.extend(p66[:])
p.extend(p67[:])
p.extend(p68[:])
p.extend(p69[:])
p.extend(p70[:])
p.extend(p71[:])
p.extend(p72[:])
p.extend(p73[:])
p.extend(p74[:])

t = range(0,9990)
figure(1,figsize=(20,10))
plot(t,p)

#write out sample----------------------
"savetxt('sample.txt',Alls,fmt='%s')"
"Need to delete b' and \n' in file."

#problem sample------------------------

