import json
import urllib2
import math
import pyaudio
import sys
import time

def getRate():
	content = urllib2.urlopen("http://blockchain.info/de/ticker").read()
	data = json.loads(content)
	rate = data['USD']['15m']
	return(float(rate))

def playBeep(RATE, WAVE):
	PyAudio = pyaudio.PyAudio
	p = PyAudio()
	data = ''.join([chr(int(math.sin(x/((RATE/WAVE)/math.pi))*127+128)) for x in xrange(RATE)])
	stream = p.open(format =
                p.get_format_from_width(1),
                channels = 1,
                rate = RATE,
                output = True)
	for DISCARD in xrange(2):
    		stream.write(data)
	stream.stop_stream()
	stream.close()
	p.terminate()

def main():
	global lastRate
	rate = getRate()
	freq = 600
	if rate > lastRate:
		freq = 1000
	print("last: %.2f current: %.2f" % (lastRate, rate))
	if rate != lastRate:
		playBeep(8000, freq)
	lastRate = rate
	

lastRate = getRate()
while True:
	main()
	time.sleep(60)




