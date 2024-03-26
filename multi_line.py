import time
import random
import string
import emoji

# Define character sets
ascii_letters = string.ascii_letters + " "  # English letters
digits = string.digits  # Digits
punctuation = string.punctuation  # Punctuation
turkish_characters = "ğüşıöçĞÜŞİÖÇ"  # Turkish characters
emojis = "".join(emoji.EMOJI_DATA.keys())

# val = input("Enter your input: ")
val = "Aşkımsın Sudenaz 🧡 !!"
sizeOfString = len(val)


# Function to determine the appropriate character set
def determine_charset(character):
    if character.isdigit():
        return digits
    elif character in punctuation:
        return punctuation
    elif character in turkish_characters:
        return ascii_letters + turkish_characters
    elif character in emojis:
        return emojis
    else:
        return ascii_letters


for x in range(sizeOfString):
    current_char = val[x]  # The current character we are trying to guess
    charset = determine_charset(
        current_char
    )  # Determine the character set based on the current character
    tried_combinations = []  # Reset the list for each new character

    while True:
        random_char = random.choice(
            charset
        )  # Pick a random character from the appropriate set
        attempted_combination = (
            val[0:x] + random_char
        )  # Create the attempted combination
        if (
            attempted_combination not in tried_combinations
        ):  # Check if we've already tried this combination
            tried_combinations.append(
                attempted_combination
            )  # Add it to the list of tried combinations
            print(attempted_combination)  # Print the current attempted combination

            if current_char in emojis:
                time.sleep(0.001)  # Make it faster for emojis
            else:
                time.sleep(0.02)  # Keep the original speed for other character types

        if random_char == current_char:  # Check if the correct character was found
            break  # Exit the loop if the correct character is found
    # Print the correct part of the string so far, then move on to the next character
    print(val[0 : x + 1])
