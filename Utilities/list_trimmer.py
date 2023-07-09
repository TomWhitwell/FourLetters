# Open 'words.txt' and read lines
with open('30k.txt', 'r') as f:
    words = f.readlines()

# Filter out the four-letter words, remove any with punctuation and convert to uppercase
four_letter_words = [word.strip().upper() for word in words if len(word.strip()) == 4 and word.strip().isalpha()]

# Open 'four.txt' and write the four-letter words
with open('smaller-four.txt', 'w') as f:
    for word in four_letter_words:
        f.write(word + '\n')
