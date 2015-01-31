import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

StepPins = [24,25,8,7]

for pin in StepPins:
	print "Setup pins"
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)

StepCounter = 0
WaitTime = 0.05

StepCount1 = 4
Seq1 = []
Seq1 = range ( 0, StepCount1)
Seq1[0] = [1,1,0,0]
Seq1[1] = [0,1,1,0]
Seq1[2] = [0,0,1,1]
Seq1[3] = [1,0,0,1]

StepCount2 = 8
Seq2 = []
Seq2 = range ( 0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

Seq = Seq1
StepCount = StepCount1

while 11:
	for pin in range(0,4):
		xpin = StepPins[pin]
		if Seq[StepCounter][pin] !=0:
			print "Step %i Enable %i" % (StepCounter,xpin)
			GPIO.output(xpin, True)
		else:
			GPIO.output(xpin, False)
	StepCounter +=1

	if (StepCounter == StepCount):
		StepCounter = 0
	if (StepCounter < 0):
		StepCounter = StepCount

	time.sleep(WaitTime)

