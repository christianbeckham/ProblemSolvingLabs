# Task 1: Happy Numbers
# NEED TO COMPLETE TASK
happy_number = 19


def is_happy_number(number):
    # separate input numbers
    first_integer = number // 10
    second_integer = number % 10

    print('First num: ', first_integer)
    print('Second num: ', second_integer)


is_happy_number(happy_number)

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

print('\nPrime numbers from 1-100:')
print(all_prime_numbers)

# Task 3 Fibonacci
fib_sequence = []
fib_start = 1
fib_sequence_limit = 10


def fibonacci_sequence(start_number, limit):
    if len(fib_sequence) == limit:
        return

    if len(fib_sequence) <= 1:
        fib_sequence.append(start_number + 0)
    else:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
        start_number = next_number

    fibonacci_sequence(start_number, limit)


print(f'\nFirst {fib_sequence_limit} fibonacci numbers')
fibonacci_sequence(fib_start, fib_sequence_limit)
print(fib_sequence)


# Task 4: Fibonacci - Harder version
# write method that does the Fibonacci sequence starting from a user input

start_input = int(input('\nEnter a number to start a Fibonacci sequence: '))
user_fib_sequence = []


def create_fib_sequence(number, stop=10):
    array_length = len(user_fib_sequence)

    if array_length == stop:
        return

    if array_length <= 1:
        user_fib_sequence.append(number + 0)
    else:
        number = user_fib_sequence[-1] + user_fib_sequence[-2]
        user_fib_sequence.append(number)

    create_fib_sequence(number)


create_fib_sequence(start_input)
print(user_fib_sequence)
