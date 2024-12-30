def is_palindrome(text):
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]

user_input = input("Enter some text: ")
if user_input == "":
    print("Empty string is not a palindrome")
elif is_palindrome(user_input):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

