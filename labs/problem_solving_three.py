# Task 1: Happy Numbers


def sum_of_square_numbers(number):
    sum = 0
    for num in str(number):
        sum += int(num) * int(num)
    return sum


def is_happy_number(number):
    list_of_numbers_checked = [number]

    while number != 1:
        number = sum_of_square_numbers(number)

        if number in list_of_numbers_checked:
            return False

        list_of_numbers_checked.append(number)

    return True


happy_number = 19
result = is_happy_number(happy_number)
print(f'Task 1: Is {happy_number} a happy number... {result}')

# Task 2: Prime Numbers


def check_is_prime(number):
    prime_boolean = False

    if number == 1:
        return prime_boolean

    for iter in range(2, number):
        if number % iter == 0:
            return prime_boolean

    prime_boolean = True
    return prime_boolean


all_prime_numbers = []
for num in range(1, 101):
    is_prime = check_is_prime(num)

    if is_prime:
        all_prime_numbers.append(num)

print('\nTask 2:')
print('Prime numbers from 1-100:', all_prime_numbers)

# Task 3 Fibonacci


def generate_fibonacci_sequence(start_number, range_limit):
    fibonacci_list = [start_number]

    for index in range(range_limit):
        if index == 0:
            fibonacci_list.append(fibonacci_list[index] + 0)
        else:
            fibonacci_list.append(
                fibonacci_list[index] + fibonacci_list[index - 1])

    return fibonacci_list


start_number = 1
range_limit = 10
result = generate_fibonacci_sequence(start_number, range_limit)
print('\nTask 3: Fibonacci sequence starting at 1 -', result)


# Task 4: Fibonacci - Harder version
# write method that does the Fibonacci sequence starting from a user input

start_number_input = int(
    input('\nEnter a number to start a Fibonacci sequence: '))
range_limit = 15
result = generate_fibonacci_sequence(start_number_input, range_limit)
print(f'\nTask 4: Fibonacci sequence starting at {start_number_input}', result)
