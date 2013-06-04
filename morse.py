import RPi.GPIO as GPIO
import time

#LED is connected to pin 1
pinNum = 1 
#dashes are twice as long as dots
dashlen = 1
dotlent = dashlen/2
#Time to wait between each signal
wait = 0.2
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pinNum,GPIO.OUT) 

#Dictionary for converting from letters to morse code
CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

def dash():
	GPIO.output(pinNum,GPIO.HIGH)
	time.sleep(dashlen)
	GPIO.output(pinNum,GPIO.LOW)
	time.sleep(wait)
	
def dot():
	GPIO.output(pinNum,GPIO.HIGH)
	time.sleep(dashlen)
	GPIO.output(pinNum,GPIO.LOW)
	time.sleep(wait)


#Interpret string and convert to morse code
while True:
	input = raw_input('please enter message: ')
	input.upper()
	
	for letter in input:
		for symbol in CODE[letter]:
			if symbol == '-':
				dash()
			elif symbol == '.':
				dot()
			else :
				time.sleep(wait)
		time.sleep(wait)
