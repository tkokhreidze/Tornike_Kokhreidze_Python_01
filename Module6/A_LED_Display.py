def seven_segment_display(number):
    digits = {
        '0': [" ### ", "#   #", "#   #", "#   #", " ### "],
        '1': ["  #  ", " ##  ", "  #  ", "  #  ", "#####"],
        '2': [" ### ", "#   #", " ### ", "#    ", "#####"],
        '3': [" ### ", "   #", " ### ", "   #", " ### "],
        '4': ["#   #", "#   #", "#####", "  #  ", "  #  "], 
        '5': ["#####", "#    ", "#####", "    #", "#####"],
        '6': [" ### ", "#    ", "#####", "#   #", " ### "],
        '7': ["#####", "#   #", "   # ", "  #  ", "  #  "],
        '8': [" ### ", "#   #", " ### ", "#   #", " ### "],
        '9': [" ### ", "#   #", " ### ", "  #  ", " ### "], 
        ':': ["   ", " # ", "   ", " # ", "   "]
    }

    # Convert the number to a string to iterate over each digit
    number_str = str(number)

    # Initialize the display lines
    display_lines = ["", "", "", "", ""]

    # Build the display lines for each digit
    for digit in number_str:
        pattern = digits[digit]
        for i in range(5):
            display_lines[i] += pattern[i] + " "

    # Print the display lines
    for line in display_lines:
        print(line)

# Get user input
number = input("Enter a non-negative integer: ")
seven_segment_display(number)
