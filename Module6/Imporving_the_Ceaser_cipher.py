def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 25.")


text = input("Enter text to encrypt: ")
shift = get_valid_shift()
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)
