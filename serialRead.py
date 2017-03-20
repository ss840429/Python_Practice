import serial
import matplotlib.pyplot as plt

fig, (axH, axa) = plt.subplots(2,1)

time = 0.1
lastH = 0
lastA1, lastA2, lastA3 = 0, 0, 0
lastAx, lastAy, lastAz = 0, 0, 0
lasttimeA = 0
lasttimeH = 0

with serial.Serial('COM9', 9600, timeout=2) as s:
	while True:
		line = s.readline().decode('utf-8') 
		time += 0.1

		if time > 200:
			break
		if line.startswith('Acce : '):
			line = line[len('Acce : '):]
			acc = line.split(' ')
			try:
				ax, ay, az = float(acc[0]), float(acc[1]), float(acc[2])
			except:
				continue
			if lastA1 != 0 and lastAx != lastA1 :
				axa.plot([lasttimeA, time], [lastAx, ax-lastA1], color='r')
				axa.plot([lasttimeA, time], [lastAy, ay-lastA2], color='g')
				axa.plot([lasttimeA, time], [lastAz, az-lastA3], color='b')

			lastAx, lastAy, lastAz = ax-lastA1, ay-lastA2, az-lastA3
			lastA1, lastA2, lastA3 = ax, ay, az
			lasttimeA = time

		if line.startswith('Heartrate : '):
			line = line[len('Heartrate : '):len('Heartrate : ')+3]
			h = float(line)
			if lastH != 0 :
				axH.plot([lasttimeH, time], [lastH, h], color='r')
				print([lasttimeH, time], [lastH, h])
			lasttimeH = time
			lastH = h

	s.close()

plt.show()
