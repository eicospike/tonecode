#!/usr/bin/env python2.7

import wave
import numpy as np
from numpy import fft
from pylab import *



wr = wave.open('Noise.wav', 'rb')
sz = 21184100
da = np.fromstring(wr.readframes(sz), dtype=np.int16)
left, right = da[0::2], da[1::2]
l = len(left)
r = len(right)
x = np.arange(l)
y = np.arange(r)
g = len(x)
h = len(y)

tt = 0
tt2 = 240
for t in range(0,600):
        EE = left[tt:tt2]
        tt = tt + 240
        tt2 = tt2 + 240
        lf, rf = np.fft.rfft(EE), np.fft.rfft(right)
        if abs(lf[11]) > 2200000:
                print 0
        if abs(lf[13]) > 2000000:
                print 1

