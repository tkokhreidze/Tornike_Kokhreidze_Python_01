def find_word(word, text):
    pos = 0
    for char in word:
        pos = text.find(char, pos)
        if pos == -1:
            return "No"
        pos += 1
    return "Yes"

word = input("Enter the word to find: ")
text = input("Enter the text to search in: ")

print(find_word(word, text))
