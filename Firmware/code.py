import random
import time
import gc
from sys import stdout

## FUNCTIONS 

class RotatingSet:
    def __init__(self, size):
        self.size = size
        self.data = []

    def add(self, item):
        if item not in self.data:
            if len(self.data) == self.size:
                self.data.pop(0)
            self.data.append(item)

    def __contains__(self, item):
        return item in self.data

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)


def print(*args, **kwargs):
    pass
    
def print2(content):
# 	stdout.write(content)
# 	stdout.write("\n")
	pass

def pick_random_word(wordList):
	selected_word = None
	with open(wordList, 'r') as file:
		for i, line in enumerate(file):
			if random.randint(0, i) == 0:
				selected_word = line.strip()
	return selected_word

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

def replace_position(s, pos):
	return s[:pos] + "*" + s[pos+1:]
	
import board
from digitalio import DigitalInOut, Direction
import time
# Define the pins you'll be using:
pins = {
	'WR': DigitalInOut(board.GP27),
	'A0': DigitalInOut(board.GP29),
	'A1': DigitalInOut(board.GP28),
	'BL': DigitalInOut(board.GP7),
	'D': [DigitalInOut(board.GP0), DigitalInOut(board.GP1), DigitalInOut(board.GP2), DigitalInOut(board.GP3), DigitalInOut(board.GP6), DigitalInOut(board.GP5), DigitalInOut(board.GP4)],
}

# Set the direction of the pins:
for pin_name, pin in pins.items():
	if pin_name != 'D':
		pin.direction = Direction.OUTPUT
	else:
		for d_pin in pin:
			d_pin.direction = Direction.OUTPUT

pins['BL'].value = True

## function to refresh display 

# Function to write a byte to the display:
def write_to_display(byte, address):
	# Set address pins
	pins['A1'].value = (address >> 1) & 0x01
	pins['A0'].value = address & 0x01
	# Set data pins
	for i in range(7):
		pins['D'][i].value = (byte >> i) & 0x01

	# Toggle WR to write
	pins['WR'].value = False
	time.sleep(0.001)  # wait for 1ms
	pins['WR'].value = True

# Function to display a character at a specific position:
def display_char(char, position):
	write_to_display(ord(char), position)

# Function to display a whole four letter word 
def display_word(random_word):
	display_char(random_word[0],3)
	display_char(random_word[1],2)
	display_char(random_word[2],1)
	display_char(random_word[3],0)

## VARIABLES 

wordList = "four.txt"
delayTime = 2 

history_set = RotatingSet(100)
word_set = set()
with open(wordList, 'r') as file:
	for line in file:
		word_set.add(line.strip())
words_len = len(word_set)

## MAIN LOOP  

# pick a word to start with 
random_word = pick_random_word(wordList).strip()

# Print the initial word
print(random_word)

 
while(True):
	cursor = random.randint(0, 3)
	cursor_tries = 0
	found = False
	while not found:
			i = 1
			while i <= 26:
				# Calculate the ASCII value of the new letter
				ascii_val = (ord(random_word[cursor]) - ord('A') + i) % 26 + ord('A')
			
				# Replace the character at the cursor with the new letter
				new_word = random_word[:cursor] + chr(ascii_val) + random_word[cursor+1:]
				print("Rotating {}, cursor position {} try {} = {}".format(random_word, cursor, i, new_word))
			
				# Check if the new word is in the set of four-letter words
				if random_word != new_word and new_word in word_set and new_word not in history_set:
					print("Found: {}".format(new_word))

					random_word = new_word 
					found = True
					print(replace_position(random_word, cursor))
					display_word(replace_position(random_word, cursor))
					time.sleep(delayTime * 0.25)
					break
				i += 1
			# If we haven't found a new word, move to the next cursor position
			if not found:
				cursor = (cursor + 1) % 4
				print("Shifting to cursor position {}, try number {}".format(cursor, cursor_tries))

				cursor_tries += 1

			# If we've tried all cursor positions and haven't found a new word, choose a new random word
			if cursor_tries >= 4:
				random_word = pick_random_word(wordList).strip()
				print("****")
				display_word("****")

				time.sleep(delayTime * 0.25)
				break

	print(random_word)
	print2(str(len(history_set)) + " " +  str(gc.mem_free()))
	display_word(random_word)
	time.sleep(delayTime*2)
	history_set.add(random_word)
	if (len(history_set) == len(word_set)):
		history_set = set()
 
