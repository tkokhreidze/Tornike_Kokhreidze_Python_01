import datetime
import time
import os

def display_time_in_blocks(time_str):
    """Displays time in block letters."""

    digits = {
        '0': [" ### ", "#   #", "#   #", "#   #", " ### "],
        '1': ["  #  ", " ##  ", "  #  ", "  #  ", "#####"],
        '2': [" ### ", "#   #", " ### ", "#    ", "#####"],
        '3': [" ### ", "#   #", " ### ", "#   #", " ### "],
        '4': ["#   #", "#   #", "#####", "  #  ", "  #  "], 
        '5': ["#####", "#    ", "#####", "    #", "#####"],
        '6': [" ### ", "#    ", "#####", "#   #", " ### "],
        '7': ["#####", "#   #", "   # ", "  #  ", "  #  "],
        '8': [" ### ", "#   #", " ### ", "#   #", " ### "],
        '9': [" ### ", "#   #", " ### ", "  #  ", " ### "], 
        ':': ["   ", " # ", "   ", " # ", "   "]
    }

    lines = ["", "", "", "", ""]

    for char in time_str:
        if char in digits:
            digit_blocks = digits[char]
            for i in range(5):
                lines[i] += digit_blocks[i] + "  "  
        else:
            for i in range(5):
                lines[i] += "     "  

    for line in lines:
        print(line)

while True:
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")

    os.system('cls' if os.name == 'nt' else 'clear')

    print("CURRENT TIME")
    display_time_in_blocks(time_str)
    time.sleep(1)