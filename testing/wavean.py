#!/usr/bin/env python2.7

import wave
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
from pylab import *

from tempfile import TemporaryFile
npout = TemporaryFile()




#dt=np.dtype('i')
wr = wave.open('Noise.wav', 'rb')
sz = 1184100
da = np.fromstring(wr.readframes(sz), dtype=np.int16)
left, right = da[0::2], da[1::2]
l = len(left)
r = len(right)
x = np.arange(l)
y = np.arange(r)
g = len(x)
h = len(y)





tt = 0

tt2 = 133
for t in range(0,103):
        EE = left[tt:tt2]
        tt = tt + 100
        tt2 = tt2 + 100
        lf, rf = np.fft.rfft(da), np.fft.rfft(EE)
        if abs(rf[6]) > 2000000:
            print 0
        if abs(rf[7]) > 2000000:
            print 1
        
#print x,da
#print g,h,lf

plt.figure(1)
a = plt.subplot(211)
r = 2**16
a.set_ylim([-32200, -32210])
a.set_xlabel('time [s]')
a.set_ylabel('sample value [-]')
plt.plot(y, left)

b = plt.subplot(212)
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
b.set_ylabel('|amplitude|')
plt.plot(abs(rf))

plt.figure(2)
c = plt.subplot(211)
c.set_ylim([30755, 33070])
c.set_xlabel('time [s]')
c.set_ylabel('sample value [-]')
plt.plot(y, left)


    
#info = np.asarray(left)

#np.savetxt("npout.txt", info)
#np.savetxt("npout.bin", left)

posleft = [0]
B = [0]
C = [0]
D = [0]
E = [0]
t=0
for t in range(0, 24960):
    if left[t] > 0:
        posleft.append(left[t])

#print posleft
BB = left[0:238]

for t in range(0, 238):
    if BB[t] > 0:
        B.append(BB[t])

CC = left[238:476]
t=0
for t in range(0, 238):
    if CC[t] > 0:
        C.append(CC[t])

DD = left[476:714]
t=0
for t in range(0, 238):
    if DD[t] > 0:
        D.append(DD[t])

EE = left[1968:2624]
t=0
for t in range(0, 656):
    if EE[t] < -30000:
        E.append(EE[t])

BA = np.average(B)
CA = np.average(C)
DA = np.average(D)
EA = np.average(E)

#print BA
#print CA
#print DA
#print EA

#print E
#print l



plt.show()