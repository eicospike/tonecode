echo "$1"|minimodem --tx --alsa --ascii -f Noise.wav 100


echo `./wavean2.py` |tr -d ' '|cut -c 4- | sed 's|..........|&\n|g'|sed 's|.| |8'|sed 's|.| |9'|sed 's|.| |10'|rev|sed 's/^ *//'>wavedump.bin

./prepare.x wavedump.bin

