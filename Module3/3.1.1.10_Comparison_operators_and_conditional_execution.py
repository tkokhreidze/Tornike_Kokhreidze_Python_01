input_string = str(input("Write a word: "))

if "Spathiphyllum" in input_string:
    print("Yes - Spathiphyllum is the best plant ever!")
elif "spathiphyllum" in input_string:
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {input_string}!")
