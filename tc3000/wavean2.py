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
da = np.fromstring(wr.readframes(sz), dtype=np.int16)
left = da[0::2]
l = len(left)
x = np.arange(l)
g = len(x)
z = sys.argv[1]
zz = int(z)
zz = zz * 10
zzz = 8
t = 0
tt = 0
tt2 = zzz
for t in range(0,zz):
        EE = left[tt:tt2]
        tt = tt + zzz
        tt2 = tt2 + zzz
        lf = np.fft.rfft(EE)

        avg = abs(lf[1]) + abs(lf[3])
        avg = avg / 2



#        if (abs(lf[2]) > 73100) or (abs(lf[1]) < 97587):
#                print 1
#        if (abs(lf[1]) > 91000) and (abs(lf[2]) < 45000):
#                print 0
        if (abs(lf[2]) < avg):
            print 0
        else:
            print 1
