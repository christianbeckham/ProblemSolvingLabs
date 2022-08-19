# Tasks
# Task 1: Reverse a String
def reverse_string(string):
    new_string = ''

    for index in range(len(string) - 1, -1, -1):
        new_string += string[index]

    return new_string


string_to_reverse = 'Hello'
result = reverse_string(string_to_reverse)
print('\nTask 1 result: ', result)

# Task 2: Capitalize a Letter


def capitalize_every_first_letter(phrase):
    new_phrase = ''

    for word in phrase.split(' '):
        new_phrase += word.capitalize()
        new_phrase += ' '

    return new_phrase


phrase = 'hello world'
result = capitalize_every_first_letter(phrase)
print('\nTask 2 result: ', result)

# Task 3: Palindrome


def reverse_string(string):
    new_string = ''

    for index in range(len(string) - 1, -1, -1):
        new_string += string[index]

    return new_string


def remove_non_alphabetic_characters(string):
    new_string = ''

    for char in string:
        if char.isalpha():
            new_string += char

    return new_string


def check_is_palindrome(string):
    string_characters_only = remove_non_alphabetic_characters(string)
    reversed_string = reverse_string(string)
    reversed_string_characters_only = remove_non_alphabetic_characters(
        reversed_string)

    if string_characters_only == reversed_string_characters_only:
        return True
    else:
        return False


user_input = input("\nEnter a palindrome word to check: ")
result = check_is_palindrome(user_input)
print(f'Task 3: Is {user_input} a palindrome... {result}')

# Bonus Challenge
# Task 4 : Compress a string of characters


def compress_characters(string):
    compressed_string = ''
    count = 1

    for index in range(len(string)):
        if index < len(string) - 1 and string[index] == string[index + 1]:
            count += 1
        else:
            sequence = str(count) + string[index]
            compressed_string += sequence
            count = 1

    return compressed_string


characters_to_compress = 'aaabbbbbccccaacccbbbaaabbbaaa'
result = compress_characters(characters_to_compress)
print('\nTask 4 results: ', result)
