# max tonr 96,000
#12000 appears to works and it relies on overlapping the fft sample
#overlaping yes but still sampled in the correct spot....
# this was done with a plus one to the width of the sample
#_________________________________________________________________________
#minimodem: simple-tone-generator.c:172: simpleaudio_tone: 
#Assertion `simpleaudio_write(sa_out, buf, nsamples_dur) > 0' failed.
#Aborted (core dumped)
#
#
#changes needed in tone detection in wavean2.py
#changes needed here to process the data for prepare




echo "$1"|minimodem --tx --alsa --ascii -f Noise.wav 12000


echo `./wavean2.py $(echo "$1"|wc -c)` |tr -d ' '|cut -c 3-|sed 's|..........|&\n|g'|sed 's|.| |9'|sed 's|.| |1'|sed 's|.| |10'|tr -d ' '|rev|sed 's/^ *//'>wavedump.bin



#echo `./wavean2.py $(echo "$1"|wc -c)` |tr -d ' '|cut -c 3- | sed 's|..........|&\n|g'|sed 's|.| |8'|sed 's|.| |9'|sed 's|.| |10'|rev|sed 's/^ *//'>wavedump.bin

#echo `./wavean2.py $(echo "$1"|wc -c)` |tr -d ' '|sed 's|..........|&\n|g'|sed 's|.| |8'|sed 's|.| |9'|sed 's|.| |10'|rev|sed 's/^ *//'>wavedump.bin


./prepare.x wavedump.bin

#need to fix the fft error
