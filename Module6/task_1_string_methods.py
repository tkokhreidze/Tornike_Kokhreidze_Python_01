def demonstrate_string_methods():
    sample_string = "hello world"
    numeric_string = "12345"
    uppercase_string = "HELLO"
    whitespace_string = "   hello   "
    formatted_string = "hello\tworld"
    multiline_sample_string = "hello\nworld"
    mixed_characters_string = "hello123"

    print(sample_string.capitalize())
    print(sample_string.casefold())
    print(sample_string.center(20, '*'))
    print(sample_string.count('o'))
    print(sample_string.encode())
    print(sample_string.endswith('d'))
    print(formatted_string.expandtabs(4))
    print(sample_string.find('o'))
    print("Hello {}!".format("world"))
    print("Hello {name}!".format_map({"name": "world"}))
    print(sample_string.index('o'))
    print(mixed_characters_string.isalnum())
    print(sample_string.isalpha())
    print(sample_string.isascii())
    print(numeric_string.isdecimal())
    print(numeric_string.isdigit())
    print(sample_string.isidentifier())
    print(sample_string.islower())
    print(numeric_string.isnumeric())
    print(sample_string.isprintable())
    print("   ".isspace())
    print("Hello World".istitle())
    print(uppercase_string.isupper())
    print(", ".join(["hello", "world"]))
    print(sample_string.ljust(20, '*'))
    print(sample_string.lower())
    print(whitespace_string.lstrip())
    print(sample_string.maketrans("h", "H"))
    print(sample_string.partition(' '))
    print(sample_string.replace('world', 'there'))
    print(sample_string.rfind('o'))
    print(sample_string.rindex('o'))
    print(sample_string.rjust(20, '*'))
    print(sample_string.rpartition(' '))
    print(sample_string.rsplit(' '))
    print(sample_string.rstrip())
    print(sample_string.split(' '))
    print(multiline_sample_string.splitlines())
    print(sample_string.startswith('h'))
    print(sample_string.strip())
    print(sample_string.swapcase())
    print(sample_string.title())
    print(sample_string.translate(sample_string.maketrans("h", "H")))
    print(sample_string.upper())
    print(sample_string.zfill(20))

demonstrate_string_methods()