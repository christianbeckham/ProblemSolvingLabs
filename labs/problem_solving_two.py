# Tasks
# Task 1: Reverse a String
string = 'Hello'
reversed_string = string[::-1]
print('\nTask 1 result: ', reversed_string)

# OR
string = 'Hello'
temp_character_array = []

for char in string:
    temp_character_array.insert(0, char)

reversed_string_two = ''.join(temp_character_array)
print('\nTask 1 result 2: ', reversed_string_two)

# Task 2: Capitalize a Letter
string = 'hello world'
temporary_string_array = []
separator = ' '

split_string = string.split(separator)

for word in split_string:
    temporary_string_array.append(word[0].capitalize() + word[1::])

final_string = separator.join(temporary_string_array)
print('\nTask 2 results: ', final_string)

# Task 3: Palindrome
user_input = input("\nEnter a palindrome word to check: ")
user_input_backwards = user_input[::-1]

if user_input == user_input_backwards:
    print(f'\tTask 3 results: The word {user_input} is a palindrome.')
else:
    print(f'\tTask 3 results: The word {user_input} is NOT a palindrome.')

# Bonus Challenge
# Task 4 : Compress a string of characters
characters = 'aaabbbbbccccaacccbbbaaabbbaaa'
compressed_characters = ''
letter_count = 1

for index in range(len(characters)):
    current_letter = characters[index]

    if index < (len(characters) - 1):
        next_letter = characters[index + 1]
    else:
        next_letter = ''

    if next_letter == current_letter:
        letter_count += 1
    else:
        output = str(letter_count) + current_letter
        compressed_characters += output
        letter_count = 1

print('\nTask 4 results: ', compressed_characters)
