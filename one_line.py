import time
import random
import string

# Define the list of characters to include letters, digits, and punctuation
all_characters = string.ascii_letters + string.digits + string.punctuation + " "

val = input("Enter your input: ")
sizeOfString = len(val)

for x in range(sizeOfString):
    tried_letters = []  # Reset the list for each new character
    current_char = val[x]  # The current character we are trying to guess
    while True:
        random_char = random.choice(
            all_characters
        )  # Pick a random character from our list
        if (
            random_char not in tried_letters
        ):  # Check if we've already tried this character
            tried_letters.append(random_char)  # Add it to the list of tried characters
            print(
                f"\r{val[0:x]}{random_char}" + " " * (sizeOfString - x - 1),
                end="",
                flush=True,
            )  # Print the current attempt
            time.sleep(0.05)
        if random_char == current_char:  # Check if the correct character was found
            break  # Exit the loop if the correct character is found
    print(
        f"\r{val[0:x + 1]}" + " " * (sizeOfString - x - 1), end="", flush=True
    )  # Print the correct part of the string so far
print()  # Print a newline at the end of the process
