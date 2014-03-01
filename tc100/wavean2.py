#!/usr/bin/env python2.7
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
t = 0
tt = 0
tt2 = 240
for t in range(0,zz):
        EE = left[tt:tt2]
        tt = tt + 240
        tt2 = tt2 + 240
        lf = np.fft.rfft(EE)
        if abs(lf[11]) > 2200000:
                print 0
        if abs(lf[13]) > 2000000:
                print 1
