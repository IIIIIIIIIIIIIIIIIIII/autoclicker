import subprocess
import time
import random
import sys

try:
	alch_arg = sys.argv[1]
except:
	alch_arg = 2**16


def alching(alch=alch_arg):

	random.seed() # initialize random seed generator - use current system time as the hashable object
	for i in range(0,int(alch)):
		print "Alch: " + str(i) + " / " + str(alch)
	# move mouse over the correct point on the screen
	# use the 'xdotool getmouselocation' command in terminal to get coordinates for current location
	#mouse_X = 784
	#mouse_Y = 294
	#subprocess.call(["xdotool", "mousemove", str(mouse_X), str(mouse_Y)])

		# press down on the mouse
		subprocess.call(["xdotool", "mousedown", "1"])
	
		# sleep for a random interval between 0.1 - 0.5 seconds
		upper_range = random.randint(300,500)
		lower_range = random.randint(100,250)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)
	
		# release mouse click
		subprocess.call(["xdotool", "mouseup", "1"])

		# random delay before next click
		upper_range = random.randint(1400,1500)
		lower_range = random.randint(900,1100)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)

		# repeat to turn off prayer
		subprocess.call(["xdotool", "mousedown", "1"])
		upper_range = random.randint(300,500)
		lower_range = random.randint(100,250)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)
		subprocess.call(["xdotool", "mouseup", "1"])
	
		# random delay before next click
		upper_range = random.randint(1400,1500)
		lower_range = random.randint(900,1100)
		time.sleep(random.randint(lower_range,upper_range) / 1000.0)

if __name__ == "__main__":
	alching()
