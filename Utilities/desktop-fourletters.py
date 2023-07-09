wordlist = "smaller-four.txt"

def replace_position(s, pos):
    return s[:pos] + "*" + s[pos+1:]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

delayTime = 2 

history_len = file_len('history.txt')
words_len = file_len(wordlist)

if history_len > words_len:
    with open('history.txt', 'w'):
        pass


import random
import time

# Open the file and get a random word
with open(wordlist, 'r') as f:
    lines = f.readlines()
    random_word = random.choice(lines).strip()

# Create a set of all four-letter words for efficient lookup
words_set = set(line.strip() for line in lines)

# Read history from 'history.txt' 
with open('history.txt', 'r') as f:
    history_lines = f.readlines()

# Create a set for efficient lookup
history_set = set(line.strip() for line in history_lines)

# Print the initial word
print(random_word)
for q in range(10000):
    # Choose a random index within the word (0-indexed)
    cursor = random.randint(0, 3)
    # Track how many cursor positions have been tried
    cursor_tries = 0
    found = False
    while not found:
        i = 1
        while i <= 26:
            # Calculate the ASCII value of the new letter
            ascii_val = (ord(random_word[cursor]) - ord('A') + i) % 26 + ord('A')
            # Replace the character at the cursor with the new letter
            new_word = random_word[:cursor] + chr(ascii_val) + random_word[cursor+1:]
            # Check if the new word is in the set of four-letter words
            if random_word != new_word and new_word in words_set and new_word not in history_set:
                random_word = new_word 
                found = True
                print("\x1b[1A", end="")
                print(replace_position(random_word, cursor))
                time.sleep(delayTime * 0.25)
                break
            i += 1

        # If we haven't found a new word, move to the next cursor position
        if not found:
            cursor = (cursor + 1) % 4
            cursor_tries += 1

        # If we've tried all cursor positions and haven't found a new word, choose a new random word
        if cursor_tries >= 4:
            random_word = random.choice(lines).strip()
            print("\x1b[1A", end="")
            print("****")
            time.sleep(delayTime * 0.25)
            break
    print("\x1b[1A", end="")

    print(random_word)
    with open('history.txt', 'a') as f:
        f.write(f'{random_word}\n')
    # Update history set
    history_set.add(random_word)
    time.sleep(delayTime * 0.75)
