![Alt](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Analogue_modem_-_acoustic_coupler.jpg/800px-Analogue_modem_-_acoustic_coupler.jpg)

ToneCode
========

tonecode


To install run

git clone https://github.com/eicospike/tonecode



To Run


./demo.x asdfaafdsafsadfasdfasdfasdfasdfsadfasdfasfasdfasdfasdfasdfasfd




Usage
-----
	$ ./demo.x shouldworkwithanyfortheb'/'softhedirectory
	shouldworkwithany100b/s
Thats all.





User Log
========

TODO:force auto detection of bitrate, prob just look for single peak fft....

some baud is in testing however appears to be working fine

Up to 12k bps and transmiting 100% from the minimal testing I have done. Bumping the rate to
24k bps seams to be imposible to make a decent fft of that little data. Possibly look at pulling
the bits from the raw sound file. Further testing with 48k bps at 48Hz sampled sound would equate
to on sample per data point, clearly an fft can't be used. Looking like 56k will take some NEW tech :)

...3000 is in testing and looks like it will be working.... this is getting close to the limit
of the fft. and samplerate of the wave.

