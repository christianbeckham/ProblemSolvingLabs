from random import randint

# LAB - PROBLEM SOLVING & RESEARCH
# Task 1: Screenshot Favorite Number
favorite_number = 10

# Task 2: Generate a Random Number
favorite_number = 10
random_number = randint(0, 20)

if random_number >= favorite_number:
    distance_away_from_favorite_number = random_number - favorite_number
else:
    distance_away_from_favorite_number = favorite_number - random_number

print(
    f'The generated random number is {random_number} and {distance_away_from_favorite_number} numbers away from your favorite number of {favorite_number}.')
