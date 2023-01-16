import time

val = input("Enter your input: ")
sizeOfString = len(val)

for x in range(sizeOfString):
    letter = 'a'
    if val[x] != ' ':
        while val[x] != letter:
            print(val[0:x], end='')
            print(letter)
            letter = chr(ord(letter)+1)
            time.sleep(0.05)
    print(val[0:x+1])