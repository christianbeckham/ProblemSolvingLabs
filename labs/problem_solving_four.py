# Task 1
# you may not use the same element twice

def find_indices_sum(numbers, target):
    num_list = list(enumerate(numbers))

    for index in range(len(num_list)):
        for key, value in num_list:
            if index != key and numbers[index] + value == target:
                return [index, key]


numbers_list = [5, 17, 77, 50]
target_number = 67

result = find_indices_sum(numbers_list, target_number)
print(f'\nTask 1: Target indices for {target_number} is {result}')

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


def sort_numbers(numbers_list):
    for _ in range(0, len(numbers_list)):
        for index in range(0, len(numbers_list) - 1):
            current_number = numbers_list[index]
            next_number = numbers_list[index + 1]

            if current_number > next_number:
                numbers_list[index] = next_number
                numbers_list[index + 1] = current_number

    return numbers_list


def check_integer_sequence(integers):
    integers_converted_to_list = list(integers)
    integers_converted_to_list_and_sorted = sort_numbers(
        integers_converted_to_list)

    for index in range(len(integers_converted_to_list_and_sorted)):
        if index == len(integers_converted_to_list_and_sorted) - 1:
            print('The provided set can form a sequence.')
            return True

        current_number = integers_converted_to_list_and_sorted[index]
        next_number = integers_converted_to_list_and_sorted[index + 1]

        if current_number + 1 != next_number:
            print('The provided set can NOT form a sequence.')
            return False


set_of_integers = {17, 15, 20, 19, 21, 16, 18}
result = check_integer_sequence(set_of_integers)
print(result)

# Task 4


def count_positive_and_add_negative(list):
    positive_number_count = 0
    sum_of_negative_numbers = 0

    for num in list:
        if num > 0:
            positive_number_count += 1
        else:
            sum_of_negative_numbers += num

    return [positive_number_count, sum_of_negative_numbers]


numbers_list = [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
result = count_positive_and_add_negative(numbers_list)
print(result)

# Task 5


def sort_numbers(numbers_list):
    for _ in range(0, len(numbers_list)):
        for index in range(0, len(numbers_list) - 1):
            current_number = numbers_list[index]
            next_number = numbers_list[index + 1]

            if current_number > next_number:
                numbers_list[index] = next_number
                numbers_list[index + 1] = current_number

    return numbers_list


def lowest_and_highest(string_of_numbers):
    final_result = ''
    list_of_numbers = string_of_numbers.split(' ')
    list_of_numbers_converted = [int(num) for num in list_of_numbers]
    list_of_numbers_converted_and_sorted = sort_numbers(
        list_of_numbers_converted)
    final_result += str(list_of_numbers_converted_and_sorted[0])
    final_result += ' '
    final_result += str(list_of_numbers_converted_and_sorted[-1])
    return final_result


number_string = '3 9 0 1 4 8 10 2'
result = lowest_and_highest(number_string)
print(result)

# Task 6: Email validation


def validate_email_address(email):
    at_sign_index = 0
    at_sign_count = 0

    for key, value in enumerate(email):
        if value == '@':
            at_sign_index = key
            at_sign_count += 1

    if 0 < at_sign_count < 2:
        username = email[0:at_sign_index]
        email_domain = email[at_sign_index + 1::]
        print('\nUsername:', username, '\nEmail domain:', email_domain)
        return True
    else:
        return False


email_address = 'christian@gmail.com'
is_valid_email_address = validate_email_address(email_address)
print(
    f'Task 6: Is {email_address} a valid email address... {is_valid_email_address}')


# Task 7
# replace characters with position in alphabet

def find_character_index_in_alphabet(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''

    for char in string:
        for key, value in enumerate(alphabet):
            if char == value:
                new_string += str(key + 1)
                break

    return new_string


string_to_replace = 'coding is fun'
result = find_character_index_in_alphabet(string_to_replace)
print('\nTask 7:', result)


# Task 8: Briefcase Lock

def calculate_shortest_rolls(number, target):
    lock_numbers = [num for num in range(0, 10)]

    if number == target:
        print(f'No rolls needed from {number} to {target}')
        return 0
    elif number > target:
        forward_rolling_list = lock_numbers[number + 1:] + lock_numbers[:target + 1]
        backward_rolling_list = lock_numbers[target:number]
    else:
        forward_rolling_list = lock_numbers[number + 1:target + 1]
        backward_rolling_list = lock_numbers[target:] + lock_numbers[:number]
        
    forward_rolls = len(forward_rolling_list)
    backward_rolls = len(backward_rolling_list)

    if forward_rolls < backward_rolls:
        print(f'Fastest roll from {number} to {target} is {forward_rolls} forward: {forward_rolling_list}')
        return forward_rolls
    else:
        print(f'Fastest roll from {number} to {target} is {backward_rolls} backwards: {backward_rolling_list}')
        return backward_rolls

    

def smallest_number_of_turns(current_combination, target_combination):
    current_combination_string = str(current_combination)
    target_combination_string = str(target_combination)
    sum_of_rolls = 0

    for index in range(len(current_combination_string)):
        current_number = int(current_combination_string[index])
        target_number = int(target_combination_string[index])
        
        roll_count = calculate_shortest_rolls(current_number, target_number)
        sum_of_rolls += roll_count

    return sum_of_rolls


current_lock_combination = 3893
target_lock_combination = 5296
result = smallest_number_of_turns(current_lock_combination, target_lock_combination)
print('\nTask 8: Total number of briefcase turns:', result)

# Task 9
