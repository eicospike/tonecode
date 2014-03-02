#changes needed in tone detection in wavean2.py
#changes needed here to process the data for prepare




echo "$1"|minimodem --tx --alsa --ascii -f Noise.wav 3000


echo `./wavean2.py $(echo "$1"|wc -c)` |tr -d ' '|cut -c 3-|sed 's|..........|&\n|g'|sed 's|.| |9'|sed 's|.| |1'|sed 's|.| |10'|tr -d ' '|rev|sed 's/^ *//'>wavedump.bin



#echo `./wavean2.py $(echo "$1"|wc -c)` |tr -d ' '|cut -c 3- | sed 's|..........|&\n|g'|sed 's|.| |8'|sed 's|.| |9'|sed 's|.| |10'|rev|sed 's/^ *//'>wavedump.bin

#echo `./wavean2.py $(echo "$1"|wc -c)` |tr -d ' '|sed 's|..........|&\n|g'|sed 's|.| |8'|sed 's|.| |9'|sed 's|.| |10'|rev|sed 's/^ *//'>wavedump.bin


./prepare.x wavedump.bin

#need to fix the fft error
