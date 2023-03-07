# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import winsound
import time

freq = 300 #Hertz
dur = 300 #Milliseconds

dashLen = dur * 3
wordPause = dur * 7

mCode = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Function for user string input
def user_phrase():
    print(f'Please type a phrase you wish to be translated:')
    userInput = input()

    return userInput

def strToMorse(strInput):
    output = ""
    strInput = strInput.upper()

    for letter in strInput:
        if letter == " ":
            output = output + "/" + " "
        else:
            output = output + mCode[letter] + " "

    return output

def morseSound(strInput):
    for code in strInput:
        if code == ".":
            winsound.Beep(freq,dur)
        elif code == "-":
            winsound.Beep(freq,dashLen)
        elif code == " ":
            time.sleep(dashLen/1000)
        else:
            time.sleep(wordPause/1000)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uInput = strToMorse(user_phrase())
    print(uInput)
    morseSound(uInput)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
