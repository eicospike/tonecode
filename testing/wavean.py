#!/usr/bin/env python2.7
#Just for testing on new faster baud rates limit of fft is close?
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



zzz = 60

tt = 0

tt2 = zzz
for t in range(0,55):
        EE = left[tt:tt2]
        tt = tt + zzz
        tt2 = tt2 + zzz
        lf, rf = np.fft.rfft(da), np.fft.rfft(EE)
        if abs(rf[2]) > 900000:
            print 0
        if abs(rf[3]) > 900000:
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

#print BA
#print CA
#print DA
#print EA

#print E
#print l



plt.show()
