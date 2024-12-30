def are_anagrams(text1, text2):
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    
    return sorted(text1) == sorted(text2)


text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

if are_anagrams(text1, text2):
    print("Anagrams")
else:
    print("Not anagrams")
