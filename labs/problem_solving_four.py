# Task 1
# you may not use the same element twice

def find_target_indices(numbers, target):
    output = []
    total_numbers = len(numbers)

    for index in range(total_numbers):
        temp_numbers = []
        placeholder = 0
        current_number = numbers[index]

        # replacing current number at index position with 0
        if index == 0:
            temp_numbers.append(placeholder)
            temp_numbers += numbers[index + 1:]
        elif 0 < index < total_numbers - 1:
            temp_numbers += numbers[:index]
            temp_numbers.append(placeholder)
            temp_numbers += numbers[index + 1:]
        elif index == total_numbers - 1:
            temp_numbers += numbers[:index]
            temp_numbers.append(placeholder)

        for index_two in range(len(temp_numbers)):
            sum = current_number + temp_numbers[index_two]

            if sum == target:
                output.append(index)
                output.append(index_two)
                return output


given_numbers = [5, 17, 77, 50]
target = 55

result = find_target_indices(given_numbers, target)
print(f'\nTask 1: Target indices for {target} is {result}')

# Task 2: Palindrome


def check_palindrome(text):
    temp_text = ''

    for char in text:
        new_char = char.lower()
        if new_char.isalpha():
            temp_text += new_char

    forward_text = temp_text
    backward_text = forward_text[::-1]

    if forward_text == backward_text:
        return True
    else:
        return False


# palindrome_word = 'level'
# palindrome_phrase = 'Mr. Owl ate my metal worm'
user_input = input('\nTask 2: Palindrome: \nPlease enter a palindrome: ')

result = check_palindrome(user_input)
print('Palindrome result is', result)

# Task 3: Check sequence of incrementing integers


# Task 4
# Task 5
# Task 6: Email validation
# Task 7
# Task 8: Briefcase Lock
# Task 9
