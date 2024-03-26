import time
import random
import string
import emoji

# Define different sets of characters
ascii_characters = string.ascii_letters + " "  # Include space as requested
turkish_characters = "ğüşıöçĞÜŞİÖÇ "  # Turkish characters including space
digits = string.digits
punctuation = string.punctuation
emojis = "".join(emoji.EMOJI_DATA.keys())

# val = input("Enter your input: ")
val = "Aşkımsın Sudenaz 🧡 !!"
sizeOfString = len(val)

for x in range(sizeOfString):
    current_char = val[x]  # The current character we are trying to guess

    # Determine the appropriate character set
    if current_char in ascii_characters or current_char in turkish_characters:
        char_set = ascii_characters + turkish_characters
    elif current_char in digits:
        char_set = digits
    elif current_char in punctuation:
        char_set = punctuation
    elif current_char in emojis:
        char_set = emojis
    else:
        char_set = (
            string.ascii_letters + " "
        )  # Fallback if the character does not fit any known category

    tried_characters = []  # Reset the list for each new character

    while True:
        random_char = random.choice(
            char_set
        )  # Pick a random character from the appropriate set
        if (
            random_char not in tried_characters
        ):  # Check if we've already tried this character
            tried_characters.append(
                random_char
            )  # Add it to the list of tried characters
            print(
                f"\r{val[0:x]}{random_char}" + " " * (sizeOfString - x - 1),
                end="",
                flush=True,
            )  # Print the current attempt

            if current_char in emojis:
                time.sleep(0.001)  # Make it faster for emojis
            else:
                time.sleep(0.02)  # Keep the original speed for other character types

        if random_char == current_char:  # Check if the correct character was found
            break  # Exit the loop if the correct character is found
    print(
        f"\r{val[0:x + 1]}" + " " * (sizeOfString - x - 1), end="", flush=True
    )  # Print the correct part of the string so far
print()  # Print a newline at the end of the process
