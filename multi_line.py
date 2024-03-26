import time
import random
import string

# Extend the characters to include uppercase, lowercase, digits, and punctuation
all_characters = string.ascii_letters + string.digits + string.punctuation + " "

val = input("Enter your input: ")
sizeOfString = len(val)

for x in range(sizeOfString):
    tried_combinations = []  # Reset the list for each new character
    current_char = val[x]  # The current character we are trying to guess
    while True:
        random_char = random.choice(all_characters)  # Pick a random character
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
            time.sleep(0.05)
        if random_char == current_char:  # Check if the correct character was found
            break  # Exit the loop if the correct character is found
    # Print all tried combinations for this character position
    for combo in tried_combinations:
        print(combo)
    # Print the correct part of the string so far, then move on to the next character
    print(val[0 : x + 1])
