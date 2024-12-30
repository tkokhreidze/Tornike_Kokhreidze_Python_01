def digit_of_life(birthday):
    while len(birthday) > 1:
        birthday = str(sum(int(digit) for digit in birthday))
    return int(birthday)

birthday = input("Enter your birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")
result = digit_of_life(birthday)
print("The Digit of Life is:", result)
