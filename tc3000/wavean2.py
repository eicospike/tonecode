#!/usr/bin/env python2.7
#this is setup for 200 baud
import sys
import os
import wave
import numpy as np
from numpy import fft
from pylab import *

statinfo = os.stat('Noise.wav')
sw = statinfo.st_size

wr = wave.open('Noise.wav', 'rb')
sz = sw*8

da = np.fromstring(wr.readframes(wr.getnframes()), dtype=np.int16)
left = da[0::1]
l = len(left)
x = np.arange(l)
g = len(x)
z = sys.argv[1]
zz = int(z)
zz = zz * 10
zzz = 16
t = 0
tt = 0
tt2 = zzz
one = 0

for t in range(0,zz):
#        one = 0
        EE = left[tt:tt2]
        tt = tt + zzz
        tt2 = tt2 + zzz
        lf = np.fft.rfft(EE)

#        avg = abs(lf[1]) + abs(lf[2])
#        avg = avg / 2
        if (abs(lf[2]) > 150000):
            print 0
#            one = 1
#        if (one < 1) and (abs(lf[1]) > 160000):
        else:
            print 1


#        if (abs(lf[2]) > 73100) or (abs(lf[1]) < 97587):
#                print 1
#        if (abs(lf[1]) > 91000) and (abs(lf[2]) < 45000):
#                print 0
#        if (abs(lf[2]) < avg):
#            print 0
#        else:
#            print 1
