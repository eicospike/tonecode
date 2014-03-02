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

samp = wr.getsampwidth()
chan = wr.getnchannels()
frames = wr.getnframes()
print wr.getframerate()
print frames
print samp
print chan
print "hello"
da = np.fromstring(wr.readframes(frames), dtype=np.int16)



left, right = da[0::1], da[1::2]
l = len(left)
r = len(right)
x = np.arange(l)
y = np.arange(r)
g = len(x)
h = len(y)

zzz = 16

tt = 0

tt2 = zzz
for t in range(0,40):
        EE = left[tt:tt2]
        tt = tt + zzz
        tt2 = tt2 + zzz
        rf = np.fft.rfft(EE)
        if (abs(rf[2]) > 140000):
            print 0
        else:
            print 1
#        avg = abs(rf[1]) + abs(rf[3])
#        print avg
#        avg = int(avg)/2
#        print avg
#        print "over"
#        print abs(rf[2])
#        if (abs(rf[2]) < avg):
#            print 0
#        else:
#            print 1


plt.figure(1)

xstart = 1
tt = 0
tt2 = zzz
start = zzz * xstart
tt = tt + start
tt2 = tt2 + start
EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

a = plt.subplot(911)
a.set_xscale('log')
a.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

b = plt.subplot(912)
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(913)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))


EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(914)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(915)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(916)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(917)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(918)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))

EE = left[tt:tt2]
tt = tt + zzz
tt2 = tt2 + zzz
lf, rf = np.fft.rfft(da), np.fft.rfft(EE)

c = plt.subplot(919)
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
plt.plot(abs(rf))










#plt.figure(2)
#c = plt.subplot(313)
#ccf.set_ylim([30755, 33070])
#cfset_xlabel('time [s]')
#ccf.set_ylabel('sample value [-]')
#plt.plot(y, left)


    
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
